from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters
from itertools import groupby

def sus(update: Update, context: CallbackContext):
    if update.effective_chat is None or update.message is None or update.message.text is None:
        return
    if 'sus' in ''.join(c for c, _ in groupby(update.message.text.lower())):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Amogus!")

sus_handler = MessageHandler(Filters.text & (~Filters.command), sus)
