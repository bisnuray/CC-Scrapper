"""
Author: Bunny
User : https://t.me/approvedccm
Channel: https://t.me/approvedccm

"""

import re
import os
import logging
import asyncio
from urllib.parse import urlparse
from aiogram import Bot, Dispatcher, types, executor
from pyrogram import Client

# Aiogram setup
BOT_TOKEN = "7153680062:AAHU5w3Nh6xAFe7Giodt5OwX1APnAuyCDvc"   # Replace this BOT_TOKEN
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Pyrogram setup
api_id = "23925218"   # Replace this API ID with your actual API ID
api_hash = "396fd3b1c29a427df8cc6fb54f3d307c"  # Replace this API ID with your actual API HASH
phone_number = "+917011352327"    # Replace this API ID with your phone number

user_client = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number)

scrape_queue = asyncio.Queue()

# Define admin user IDs
admin_ids = [5387926427,6922106594,7192604798,6572284023]

default_limit = 10000  # Max limit for any user
admin_limit = 50000    # Max limit for admin users
 
def remove_duplicates(messages):
    unique_messages = list(set(messages))
    duplicates_removed = len(messages) - len(unique_messages)
    return unique_messages, duplicates_removed

async def scrape_messages(user_client, channel_username, limit, start_number=None):
    messages = []
    count = 0

    pattern = r'\d{16}\D*\d{2}\D*\d{2,4}\D*\d{3,4}'

    async for message in user_client.search_messages(channel_username):
        if count >= limit:
            break

        text = message.text if message.text else message.caption
        if text:
            matched_messages = re.findall(pattern, text)
            if matched_messages:
                formatted_messages = []
                for matched_message in matched_messages:
                    extracted_values = re.findall(r'\d+', matched_message)
                    if len(extracted_values) == 4:
                        card_number, mo, year, cvv = extracted_values
                        year = year[-2:]
                        formatted_messages.append(f"{card_number}|{mo}|{year}|{cvv}")

                messages.extend(formatted_messages)
                count += len(formatted_messages)

    if start_number:
        messages = [msg for msg in messages if msg.startswith(start_number)]

    # Limit the messages after filtering by start_number
    messages = messages[:limit]

    return messages

async def process_scrape_queue(user_client, bot):
    while True:
        task = await scrape_queue.get()
        message, channel_username, limit, start_number, temporary_msg = task

        scrapped_results = await scrape_messages(user_client, channel_username, limit, start_number)
        
        if scrapped_results:
            unique_messages, duplicates_removed = remove_duplicates(scrapped_results)
            if unique_messages:
                file_name = f"x{len(unique_messages)}_{channel_username}.txt"
                with open(file_name, 'w') as f:
                    f.write("\n".join(unique_messages))
            
                with open(file_name, 'rb') as f:
                    caption = (
                        f"<b>CC Scrapped Successful ✅</b>\n"
                        f"<b>━━━━━━━━━━━━━━━━</b>\n"
                        f"<b>Source:</b> <code>{channel_username}</code>\n"
                        f"<b>Amount:</b> <code>{len(unique_messages)}</code>\n"
                        f"<b>Duplicates Removed:</b> <code>{duplicates_removed}</code>\n"
                        f"<b>━━━━━━━━━━━━━━━━</b>\n"
                        f"<b>Card-Scrapper By: <a href='https://t.me/approvedccm'>𝙱𝚞𝚗𝚗𝚢</a></b>\n"
                    )
                    await temporary_msg.delete()
                    await bot.send_document(message.chat.id, f, caption=caption, parse_mode='html')
                os.remove(file_name)
            else:
                await temporary_msg.delete()
                await bot.send_message(message.chat.id, "Sorry Bro ❌ No Credit Card Found")
        else:
            await temporary_msg.delete()
            await bot.send_message(message.chat.id, "Sorry Bro ❌ No Credit Card Found")
        
        scrape_queue.task_done()

@dp.message_handler(commands=['scr'])
async def scr_cmd(message: types.Message):
    args = message.text.split()[1:]
    if len(args) < 2 or len(args) > 3:
        await bot.send_message(message.chat.id, "<b>⚠️ Provide channel username and amount to scrape</b>", parse_mode='html')
        return
    
    channel_identifier = args[0]
    limit = int(args[1])
    
    # Determine the max limit based on whether the user is an admin
    max_lim = admin_limit if message.from_user.id in admin_ids else limits.get(str(message.chat.id), default_limit)

    if limit > max_lim:
        await bot.send_message(message.chat.id, f"<b>Sorry Bro! Amount over Max limit is {max_lim} ❌</b>", parse_mode='html')
        return
    
    start_number = args[2] if len(args) == 3 else None

    parsed_url = urlparse(channel_identifier)
    if parsed_url.scheme and parsed_url.netloc:
        if parsed_url.path.startswith('/+'):
            try:
                chat = await user_client.join_chat(channel_identifier)
                channel_username = chat.id
            except Exception as e:
                if "USER_ALREADY_PARTICIPANT" in str(e):
                    try:
                        chat = await user_client.get_chat(channel_identifier)
                        channel_username = chat.id
                    except Exception as e:
                        await bot.send_message(message.chat.id, f"<b>Sorry Bro! 🥲 No ccs found</b>", parse_mode='html')
                        return
                else:
                    await bot.send_message(message.chat.id, f"<b>Sorry Bro! 🥲 No ccs found</b>", parse_mode='html')
                    return
        else:
            channel_username = parsed_url.path.lstrip('/')
    else:
        channel_username = channel_identifier

    try:
        await user_client.get_chat(channel_username)
    except Exception:
        await bot.send_message(message.chat.id, "<b>Hey Bro! 🥲 Incorrect username ❌</b>", parse_mode='html')
        return
    
    temporary_msg = await bot.send_message(message.chat.id, "<b>Scraping in progress wait.....</b>", parse_mode='html')
    
    await scrape_queue.put((message, channel_username, limit, start_number, temporary_msg))

async def on_startup(dp):
    await user_client.start()
    asyncio.create_task(process_scrape_queue(user_client, bot))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
