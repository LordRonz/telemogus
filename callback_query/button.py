from telegram.ext import CallbackQueryHandler, CallbackContext
from telegram import Update


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

    rps_data = context.chat_data[f'{query.message.message_id}']
    if rps_data['p1']['id'] == query.from_user.id:
        if rps_data['p1']['choice'] is None:
            rps_data['p1']['choice'] = query.data
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"You have selected before! wait for your opponent",
            )
    elif rps_data['p2']['id'] is None:
        rps_data['p2']['id'] = query.from_user.id
        rps_data['p2']['choice'] = query.data


    query.edit_message_text(text=f"Selected option: {query.data}, {context.chat_data}")


button_handler = CallbackQueryHandler(button)
