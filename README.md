# RegistrationTelegram

A simple Telegram bot built with Pyrogram and Pyromod that asks new users for their name, age, and contact number, then stores the data in MongoDB and sends a notification to an admin.

## Features

- Handles `/start` command
- Asks users for their name and age
- Validates age input is numeric and between 1 and 99
- Requests the user's phone number using a contact button
- Stores new users in MongoDB to prevent duplicate registration
- Sends a summary of each new user to the admin chat

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

- `main.py` — bot command flow and user interaction logic
- `client.py` — Pyrogram client initialization
- `config.py` — loads environment variables via `dotenv`
- `database/users.py` — MongoDB user storage and existence checks

## Notes

- The bot currently sends collected user data to the hard-coded `ADMIN` ID inside `main.py`.
- Duplicate registrations are prevented by checking the MongoDB `users` collection.
- `CLUSTER_ID` should be a valid MongoDB connection URI for the `telebot` database.
