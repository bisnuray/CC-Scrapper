<h1 align="center">CC Scraper Telegram Bot</h1>

<p align="center">
  <a href="https://github.com/bisnuray/CC-Scrapper/stargazers"><img src="https://img.shields.io/github/stars/bisnuray/CC-Scrapper?color=blue&style=flat" alt="GitHub Repo stars"></a>
  <a href="https://github.com/bisnuray/CC-Scrapper/issues"><img src="https://img.shields.io/github/issues/bisnuray/CC-Scrapper" alt="GitHub issues"></a>
  <a href="https://github.com/bisnuray/CC-Scrapper/pulls"><img src="https://img.shields.io/github/issues-pr/bisnuray/CC-Scrapper" alt="GitHub pull requests"></a>
  <a href="https://github.com/bisnuray/CC-Scrapper/graphs/contributors"><img src="https://img.shields.io/github/contributors/bisnuray/CC-Scrapper?style=flat" alt="GitHub contributors"></a>
  <a href="https://github.com/bisnuray/CC-Scrapper/network/members"><img src="https://img.shields.io/github/forks/bisnuray/CC-Scrapper?style=flat" alt="GitHub forks"></a>
</p>

<p align="center">
  <em>CC Scraper: An advanced Telegram bot script to scrape credit cards from specified Telegram groups and channels.</em>
</p>
<hr>

## Features

- Scrapes cards from private/public Telegram groups and channels.
- Supports format: group/channel username, ID, or link.
- Scrapes specific BIN credit cards.
- Removes duplicate credit cards.
- Handles multiple requests at a time.
- Super-fast scraping speed.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher.
- `pyrofork` and `tgcrypto` libraries.
- A Telegram bot token (you can get one from [@BotFather](https://t.me/BotFather) on Telegram).
- API ID and Hash: You can get these by creating an application on [my.telegram.org](https://my.telegram.org).
- To Get `SESSION_STRING` Open [@SmartUtilBot](https://t.me/SmartUtilBot). Bot and use /pyro command and then follow all instructions.

## Installation

To install `pyrofork` and `tgcrypto`, run the following command:

```bash
pip install pyrofork tgcrypto
```

**Note: If you previously installed `pyrogram`, uninstall it before installing `pyrofork`.**

## Configuration

1. Open the `config.py` file in your favorite text editor.
2. Replace the placeholders for `API_ID`, `API_HASH`, `SESSION_STRING`, and `BOT_TOKEN` with your actual values:
   - **`API_ID`**: Your API ID from [my.telegram.org](https://my.telegram.org).
   - **`API_HASH`**: Your API Hash from [my.telegram.org](https://my.telegram.org).
   - **`SESSION_STRING`**: The session string generated using [@SmartUtilBot](https://t.me/SmartUtilBot).
   - **`BOT_TOKEN`**: The token you obtained from [@BotFather](https://t.me/BotFather).

3. Optionally, adjust the following settings:
   - **`admin_ids`**: List of admin user IDs who have elevated permissions.
   - **`admin_limit`**: The maximum number of messages admins can scrape in a single request.
   - **`default_limit`**: The maximum number of messages regular users can scrape in a single request.

## Deploy the Bot

```sh
git clone https://github.com/bisnuray/CC-Scrapper
cd CC-Scrapper
python scrapper.py
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

✨ **Note**: If you found this repo helpful, please fork and star it. Also, feel free to share with proper credit!

## Author

- Name: Bisnu Ray
- Telegram: [@itsSmartDev](https://t.me/itsSmartDev)

Feel free to reach out if you have any questions or feedback.
