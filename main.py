from subprocess import Popen
from subprocess import PIPE

from telegram import *
from telegram.ext import *
from config import TG_TOKEN
from config import TG_API_URL


def do_start(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'Братишка'
    text = f'Привет, {name}!'
    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=text,
    )


def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text='Я простой бот\n'
             'Список доступных команд есть в меню \n'
             'И пожалуйста, не стоит на меня материться...',
    )


def do_time(bot: Bot, update: Update):
    """Узнать серверное время
    """
    process = Popen('date', stdout=PIPE)
    text, error = process.communicate()
    if error:
        text = 'Произошла ошибка, время не известно'
    else:
        time = text.decode('utf-8')
        text = f'Cейчас у нас: {time}'
    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=text
    )


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'Братишка'
    text = update.effective_message.text
    reply_text = f'Прости, {name}, пока я мало что умею... ' \
                 f'\n\nПо этому просто буду тебя дразнить:' \
                 f'\n{text}'
    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )


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
    handler = MessageHandler(Filters.all, message_handler)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
