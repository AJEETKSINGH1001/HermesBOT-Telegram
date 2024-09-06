# Bilingual Telegram Bot with News Fetching Functionality

This repository contains a Python-based Telegram bot that provides an interactive and user-friendly experience in both English and Hindi. The bot supports multiple commands, allows users to select their preferred language, and fetches the latest news on any topic using NewsAPI.

## Features

- **Bilingual Support**: The bot can interact with users in both English and Hindi based on their language preference.
- **Latest News Fetching**: Fetches the latest news articles on user-specified topics using the NewsAPI.
- **Interactive Commands**: Supports commands like `/start`, `/help`, `/echo <message>`, and `/news <topic>`.
- **Language Selection**: Allows users to choose their preferred language through an interactive menu.
- **Easy to Set Up**: Built using the `python-telegram-bot` library and requires minimal setup.

## Commands

- `/start` - Start interacting with the bot and get a welcome message.
- `/help` - Show available commands and usage instructions.
- `/echo <message>` - The bot will repeat the user's message.
- `/news <topic>` - Fetch and display the latest news on a given topic.
- `/language` - Allows users to select their preferred language (English or Hindi).

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Telegram Bot Token from [BotFather](https://core.telegram.org/bots#botfather)
- News API Key from [NewsAPI](https://newsapi.org/)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/bilingual-telegram-bot.git
   cd bilingual-telegram-bot

Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file or set the environment variables in your system.

env
Copy code
TELEGRAM_TOKEN=your_telegram_bot_token
NEWS_API_KEY=your_news_api_key
Run the bot:

bash
Copy code
python telegram_bot.py
Usage
Start the Bot: Open Telegram, search for your bot by its username, and start interacting by sending the /start command.
Choose Language: Use the /language command to select your preferred language.
Get News: Use the /news <topic> command to get the latest news on a particular topic, such as /news technology.
Echo Messages: Use the /echo <message> command to make the bot repeat whatever you send.
Example Commands
/start
/help
/language
/news sports
/echo Hello, World!
Project Structure
telegram_bot.py: The main Python script containing the bot's logic and command handlers.
requirements.txt: List of dependencies required to run the bot.
Requirements
python-telegram-bot: Python wrapper for the Telegram Bot API.
requests: Library to make HTTP requests to the NewsAPI.
