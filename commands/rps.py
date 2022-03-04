from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackContext, CommandHandler


def rps(update: Update, context: CallbackContext):
    if (
        update.effective_chat is None
        or update.effective_user is None
        or context.chat_data is None
        or update.effective_message is None
    ):
        return

    if update.effective_chat.type not in ("group", "supergroup"):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"This command must be used in group or supergroup, now I'm in {update.effective_chat.type} chat",
        )
        return

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
        text=f"*Rock Paper Scissor*\n{update.effective_user.first_name} has started a rock, paper, and scissor game\! To participate, just press these buttons",
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN_V2,
    )

    context.chat_data[f"{sent_msg.message_id}"] = {
        "p1": {
            "id": update.effective_user.id,
            "name": update.effective_user.full_name,
            "choice": None,
        },
        "p2": {
            "id": None,
            "name": None,
            "choice": None,
        },
    }


rps_handler = CommandHandler("rps", rps)
