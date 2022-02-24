from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters


def unknown(update: Update, context: CallbackContext):
    if update.effective_chat is None:
        return
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.",
    )


unknown_handler = MessageHandler(Filters.command, unknown)
