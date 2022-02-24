from telegram.ext import Dispatcher
from callback_query.button import button_handler


def callback_query_handler(dispatcher: Dispatcher):
    dispatcher.add_handler(button_handler)
