from typing import Any
from telegram.ext import CallbackQueryHandler, CallbackContext
from telegram import Update

from commands.rps import rps


def get_rps_winner(rps_data: Any):
    p1 = rps_data["p1"]["choice"]
    p2 = rps_data["p2"]["choice"]
    winner = None
    if p1 == "rock":
        winner = "p1" if p2 == "scissor" else "p2"
    elif p1 == "paper":
        winner = "p1" if p2 == "rock" else "p2"
    elif p1 == "scissor":
        winner = "p1" if p2 == "paper" else "p2"

    return winner


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    if not query or not update.effective_chat:
        return

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    context.chat_data
    if not context.chat_data or query.message is None:
        return

    rps_data = context.chat_data[f"{query.message.message_id}"]
    if not rps_data:
        return

    if rps_data["p1"]["id"] == query.from_user.id:
        if rps_data["p1"]["choice"] is None:
            rps_data["p1"]["choice"] = query.data
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"{query.from_user.full_name} has chosen!",
            )
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"You have selected before! wait for your opponent",
            )
    elif rps_data["p2"]["id"] is None:
        rps_data["p2"]["id"] = query.from_user.id
        rps_data["p2"]["name"] = query.from_user.full_name
        rps_data["p2"]["choice"] = query.data

    if rps_data["p1"]["id"] is not None and rps_data["p2"]["id"] is not None:
        winner = get_rps_winner(rps_data=rps_data)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"The winner is{rps_data[winner]['name']}",
        )

        query.edit_message_text(
            text=f"The winner is{rps_data[winner]['name']}",
        )


button_handler = CallbackQueryHandler(button)
