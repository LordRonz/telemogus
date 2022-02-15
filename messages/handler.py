from telegram.ext import Dispatcher
from messages.sus import sus_handler

def message_handler(dispatcher: Dispatcher):
    dispatcher.add_handler(sus_handler)
