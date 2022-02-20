from telegram.ext import Dispatcher
from commands.start import start_handler
from commands.chat_id import chatid_handler
from commands.caps import inline_caps_handler

def command_handler(dispatcher: Dispatcher):
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(chatid_handler)
    dispatcher.add_handler(inline_caps_handler)
