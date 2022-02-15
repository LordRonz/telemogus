from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters
from itertools import groupby
from utils.utils import sus_in_string

def sus(update: Update, context: CallbackContext):
    if update.effective_chat is None or update.message is None or update.message.text is None:
        return
    if sus_in_string(update.message.text):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Amogus!")

sus_handler = MessageHandler(Filters.text & (~Filters.command), sus)
