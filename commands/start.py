from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

def start(update: Update, context: CallbackContext):
    if update.effective_chat is None:
        return
    context.bot.send_message(chat_id=update.effective_chat.id, text="Amogus!")

start_handler = CommandHandler('start', start)
