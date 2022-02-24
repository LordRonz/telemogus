from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler


def rps(update: Update, context: CallbackContext):
    if (
        update.effective_chat is None
        or update.effective_user is None
        or context.chat_data is None
        or update.effective_message is None
    ):
        return
    # if update.effective_chat.type not in ('group', 'supergroup'):
    #     context.bot.send_message(chat_id=update.effective_chat.id, text=f"This command must be used in group or supergroup, now I'm in {update.effective_chat.type} chat")
    #     return

    keyboard = [
        [
            InlineKeyboardButton("Rock", callback_data="rock"),
            InlineKeyboardButton("Paper", callback_data="paper"),
            InlineKeyboardButton("Scissor", callback_data="scissor"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    sent_msg = context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_user.first_name} has started a rock, paper, and scissor game! To participate, just press these buttons",
        reply_markup=reply_markup,
    )

    context.chat_data[f"{sent_msg.message_id}"] = {
        "p1": {
            "id": update.effective_user.id,
            "choice": None,
        },
        "p2": {
            "id": None,
            "choice": None,
        },
    }


rps_handler = CommandHandler("rps", rps)
