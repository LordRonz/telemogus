from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


def chat_id(update: Update, context: CallbackContext):
    if update.effective_chat is None:
        return
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.effective_chat.id
    )


chatid_handler = CommandHandler("chatid", chat_id)
