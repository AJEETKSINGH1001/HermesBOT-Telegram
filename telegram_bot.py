import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with the token provided by BotFather
TELEGRAM_TOKEN = '7036892727:AAFkjEFl2ofHYjQQqaHnb2S_a9IO_pxsvWI'
NEWS_API_KEY = 'fadd27bec7b04ddbbebcfe4dccf11b88'  # Replace with your NewsAPI key

# Dictionary to store user preferences
user_preferences = {}

def get_language_preference(user_id):
    """Get the language preference of the user. Default is English."""
    return user_preferences.get(user_id, 'en')

def set_language_preference(user_id, language):
    """Set the language preference of the user."""
    user_preferences[user_id] = language

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    language = get_language_preference(update.effective_user.id)
    if language == 'en':
        welcome_message = (
            "Hello! I'm your friendly Hermes bot. I can provide you with the latest news, "
            "repeat what you say, and assist you with various commands. Type /help to see what I can do!"
        )
    else:
        welcome_message = (
            "नमस्ते! मैं आपका हेमीज़ बॉट हूँ। मैं आपको ताज़ा ख़बरें दे सकता हूँ, "
            "आपके संदेश को दोहरा सकता हूँ, और विभिन्न कमांड्स के साथ आपकी मदद कर सकता हूँ। /help टाइप करें।"
        )
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    language = get_language_preference(update.effective_user.id)
    if language == 'en':
        help_text = """
        Here are the commands you can use:
        /start - Start interacting with the bot
        /help - Show help message
        /echo <message> - Repeat your message
        /news <topic> - Get the latest news on a topic (e.g., /news technology)
        /language - Choose your language preference (English or Hindi)
        """
    else:
        help_text = """
        आप निम्नलिखित कमांड्स का उपयोग कर सकते हैं:
        /start - बॉट के साथ इंटरैक्ट करना शुरू करें
        /help - मदद संदेश दिखाएँ
        /echo <संदेश> - आपका संदेश दोहराएं
        /news <विषय> - किसी विषय पर ताज़ा ख़बरें प्राप्त करें (जैसे, /news technology)
        /language - अपनी भाषा पसंद चुनें (अंग्रेजी या हिंदी)
        """
    await update.message.reply_text(help_text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    user_message = update.message.text
    language = get_language_preference(update.effective_user.id)
    if language == 'en':
        await update.message.reply_text(f'You said: {user_message}')
    else:
        await update.message.reply_text(f'आपने कहा: {user_message}')

async def get_news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Fetch and send the latest news on a given topic."""
    language = get_language_preference(update.effective_user.id)
    if context.args:
        topic = ' '.join(context.args)
        news = fetch_latest_news(topic, language)
        if news:
            await update.message.reply_text(news)
        else:
            if language == 'en':
                await update.message.reply_text(f"Sorry, I couldn't find any news on '{topic}'. Please try another topic.")
            else:
                await update.message.reply_text(f"मुझे '{topic}' पर कोई समाचार नहीं मिला। कृपया कोई अन्य विषय आज़माएँ।")
    else:
        if language == 'en':
            await update.message.reply_text("Please provide a topic to search news for. Example: /news technology")
        else:
            await update.message.reply_text("कृपया समाचार खोजने के लिए एक विषय प्रदान करें। उदाहरण: /news technology")

def fetch_latest_news(topic: str, language: str) -> str:
    """Fetch the latest news from the NewsAPI based on the given topic and language."""
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}&language={language}&pageSize=5"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if articles:
            news_list = [f"📰 {article['title']}\n{article['url']}" for article in articles]
            return "\n\n".join(news_list)
        else:
            return "No news articles found." if language == 'en' else "कोई समाचार लेख नहीं मिला।"
    else:
        return "Failed to fetch news. Please try again later." if language == 'en' else "समाचार लाने में विफल। कृपया बाद में पुनः प्रयास करें।"

async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Provide a choice for the user to select their preferred language."""
    keyboard = [
        [InlineKeyboardButton("English", callback_data='en')],
        [InlineKeyboardButton("हिन्दी", callback_data='hi')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Please choose your preferred language / कृपया अपनी पसंदीदा भाषा चुनें:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle language selection button clicks."""
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    language_choice = query.data
    set_language_preference(user_id, language_choice)
    await query.edit_message_text(text=f"Language preference set to {'English' if language_choice == 'en' else 'हिन्दी'}.")

def main() -> None:
    """Start the bot."""
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Register handlers for different commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("news", get_news))
    app.add_handler(CommandHandler("language", language_command))
    app.add_handler(CallbackQueryHandler(button))  # To handle button clicks for language selection

    # Start the bot
    app.run_polling()

if __name__ == '__main__':
    main()
