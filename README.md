<h1 align="center">CC Scrapper Telegram Bot</h1>

<p align="center">
  <a href="https://github.com/bisnuray/CC-Scrapper/stargazers"><img src="https://img.shields.io/github/stars/bisnuray/CC-Scrapper?color=blue&style=flat" alt="GitHub Repo stars"></a>
  <a href="https://github.com/bisnuray/CC-Scrapper/issues"><img src="https://img.shields.io/github/issues/bisnuray/CC-Scrapper" alt="GitHub issues"></a>
  <a href="https://github.com/bisnuray/CC-Scrapper/pulls"><img src="https://img.shields.io/github/issues-pr/bisnuray/CC-Scrapper" alt="GitHub pull requests"></a>
  <a href="https://github.com/bisnuray/CC-Scrapper/graphs/contributors"><img src="https://img.shields.io/github/contributors/bisnuray/CC-Scrapper?style=flat" alt="GitHub contributors"></a>
  <a href="https://github.com/bisnuray/CC-Scrapper/network/members"><img src="https://img.shields.io/github/forks/bisnuray/CC-Scrapper?style=flat" alt="GitHub forks"></a>
</p>

<p align="center">
  <em>CC Scrapper: An advanced Telegram bot script to scrape credit cards from specified Telegram groups and channels.</em>
</p>
<hr>

## Features

- Scrapes Cards from Private/Public Telegram groups and channels.
- Supported Format Group/Channel username/id/link
- Scrape Any Specific Bin Credit Cards
- Removes duplicate Credit Cards.
- Scraping Speed Super Fester.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher.
- `pyrogram` and `aiogram==2.6` libraries.
- A Telegram bot token (you can get one from [@BotFather](https://t.me/BotFather) on Telegram).

## Installation

To install Squid and necessary utilities, run the following commands:

```bash
pip install pyrogram
pip install aiogram==2.6
```

## Configuration

1. Open the script with your favorite text editor.
2. Find the line that contains `BOT_TOKEN = '123456:ABCDEFGHIJLLJOdMttZ5hEZ78'`.
3. Replace the placeholder token with your actual Telegram bot token.
3. Replace The `api_id`, `api_hash`, and `phone_number`
4. Optional Also you can change this `admin_ids`, `admin_limit` For Admin Scrape Limit . `default_limit` for others user

## Deploy the Bot

```sh
git clone https://github.com/bisnuray/CC-Scrapper
cd CC-Scrapper
python3 scrapper.py
```

## Usage

1. Use the `/scr` command followed by the group or channel username and the number of messages to scrape.

    ```text
    /scr @channel_username 1000
    ```

2. Optionally, you can scrape any target bin cards

    ```text
    /scr @channel_username 1000 434769
    ```

✨ **Note**: Fork this repo, & Star ☀️ the repo if you liked it. and Share this repo with Proper Credit

## Author

- Name: Bisnu Ray
- Telegram: [@itsSmartDev](https://t.me/itsSmartDev)

Feel free to reach out if you have any questions or feedback.
