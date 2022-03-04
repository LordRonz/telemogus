from utils.read_env import read_env
from utils.logger import logger
from os import getenv
from telegram.ext import Updater
from commands.handler import command_handler
from messages.handler import message_handler
from callback_query.handler import callback_query_handler
from utils.error_handler import error_handler


def main():
    read_env()

    TOKEN = getenv("TOKEN", "")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    command_handler(dispatcher)
    callback_query_handler(dispatcher)
    message_handler(dispatcher)
    dispatcher.add_error_handler(error_handler)
    logger.info("Hello World!")
    updater.start_webhook(
        listen="0.0.0.0",
        port=8443,
        url_path=TOKEN,
        webhook_url=f"https://telemogus.herokuapp.com/{TOKEN}",
    )
    updater.idle()


if __name__ == "__main__":
    main()
