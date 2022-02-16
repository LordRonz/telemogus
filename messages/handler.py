from telegram.ext import Dispatcher
from messages.sus import sus_handler
from messages.unknown import unknown_handler

def message_handler(dispatcher: Dispatcher):
    dispatcher.add_handler(sus_handler)
    dispatcher.add_handler(unknown_handler)
