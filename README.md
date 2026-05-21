# RegistrationTelegram

A simple Telegram bot built with Pyrogram and Pyromod that asks new users for their name and age, replies with a welcome message, and forwards the collected data to a configured channel.

## Features

- Listens for `/start` command
- Asks the user for their name and age using interactive questions
- Replies with a welcome message
- Sends collected user data to a Telegram channel

## Requirements

- Python 3.11+ (recommended)
- Dependencies from `requirements.txt`

## Environment Variables

The bot loads its configuration from a `.env` file. Create a `.env` file in the project root with:

```env
APP_BOT_TOKEN=your_bot_token
APP_API_ID=your_api_id
APP_API_HASH=your_api_hash
MY_CHANNEL_ID=@your_channel_username_or_id
```

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Bot

Run the bot with:

```bash
uv run reloadium run main.py
```

Or directly:

```bash
python main.py
```

## Code Overview

- `main.py` — bot logic and `/start` flow
- `authorization.py` — Pyrogram bot client initialization
- `config.py` — environment variable loading

## Notes

- The bot sends the collected name and age to `MY_CHANNEL_ID`.
- `MY_CHANNEL_ID` may be a channel username or numeric ID.
