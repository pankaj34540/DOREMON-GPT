import openai
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# OpenAI API key (environment variable se fetch kar rahe hain)
openai.api_key = os.getenv('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')

# Telegram bot API token (environment variable se fetch kar rahe hain)
TELEGRAM_API_TOKEN = os.getenv('8099461644:AAHNje3fiU53Fyoh0V95GVD8bbEXTFqsXtA')

# Function to get ChatGPT response
def chatgpt_response(prompt: str) -> str:
    try:
        response = openai.Completion.create(
            engine="gpt-4",  # GPT-4 model ka use kar rahe hain
            prompt=prompt,
            max_tokens=150,  # You can adjust this as needed
            temperature=0.7  # Control randomness
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Command handler for /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your ChatGPT bot. How can I assist you today?")

# Function to handle text messages
def respond_to_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    # Get ChatGPT response for the user's message
    response = chatgpt_response(user_message)
    update.message.reply_text(response)

# Main function to start the bot
def main() -> None:
    updater = Updater(TELEGRAM_API_TOKEN)

    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond_to_message))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if _name_ == '_main_':
    main()
