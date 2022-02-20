from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram import Update
from telegram.ext import CallbackContext

def inline_caps(update: Update, context: CallbackContext):
    if not update.inline_query:
        return

    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
