# RegistrationTelegram

A simple Telegram bot built with Pyrogram and Pyromod that asks new users for their name, age, and phone number, stores the data in MongoDB, and notifies an admin chat.

## Features

- Handles `/start` command
- Asks users for their name and age
- Validates that age is numeric and between 1 and 99
- Requests the user's phone number using a contact button
- Stores new users in MongoDB to prevent duplicate registration
- Sends a summary of each new user to an admin chat

## Requirements

- Python 3.11+
- Dependencies from `requirements.txt`

## Environment Variables

The bot loads configuration from a `.env` file in the project root. Create a `.env` file with:

```env
APP_BOT_TOKEN=your_bot_token
APP_API_ID=your_api_id
APP_API_HASH=your_api_hash
CLUSTER_ID=your_mongodb_connection_string
```

Optional environment variables loaded by `config.py` but not required by the current bot flow:

```env
DROPLINK_API_KEY=
MY_CHANNEL_ID=
```

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Bot

Run the bot directly:

```bash
python main.py
```

If you use `reloadium`, you can also run:

```bash
uv run reloadium run main.py
```

## Project Structure

- `main.py` — entry point for running the bot
- `client.py` — Pyrogram client initialization and plugin configuration
- `config.py` — loads environment variables via `dotenv`
- `plugins/start.py` — handles `/start`, user prompts, validation, and admin notifications
- `database/register_bot.py` — MongoDB connection, user insertion, and duplicate-checking logic

## Notes

- The admin notification chat ID is hard-coded in `plugins/start.py` as `ADMIN`.
- Duplicate registration is prevented by checking the MongoDB `users` collection for the user ID.
- `CLUSTER_ID` should be a valid MongoDB connection URI for the `register_bot` database.
