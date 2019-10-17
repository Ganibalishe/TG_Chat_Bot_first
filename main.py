import logging

from telegram import *
from telegram.ext import *
from config import TG_TOKEN
from config import TG_API_URL
from handlers import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def main():
    bot = Bot(
        token=TG_TOKEN,
        base_url=TG_API_URL,
    )
    updater = Updater(
        bot=bot,
    )

    start_handler = CommandHandler('start', do_start)
    help_handler = CommandHandler('help', do_help)
    time_handler = CommandHandler('time', do_time)
    love_handler = CommandHandler('love', do_love)
    handler = MessageHandler(Filters.all, message_handler)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(love_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(handler)

    unknown_handler = MessageHandler(Filters.command, unknown_commands)
    updater.dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
