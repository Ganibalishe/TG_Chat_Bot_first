from subprocess import Popen
from subprocess import PIPE
import logging

from telegram import *
from telegram.ext import *
from config import TG_TOKEN
from config import TG_API_URL

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


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


def unknown_commands(bot: Bot, update: Update):
    bot.send_message(chat_id=update.effective_chat.id, text="Простите, таких команд я не знаю...")


def do_love(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'Братишка'
    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=f'Я давно хотел сказать тебе, {name}...\n'
             f'Я люблю тебя, {name}...',
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

    love_words = ['люблю тебя', 'тебя люблю']
    for word in love_words:
        if word in text.lower():
            reply_text = f'оооооо... я тоже тебя очень люблю, {name}'

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
    love_handler = CommandHandler('love', do_love)
    unknown_handler = MessageHandler(Filters.command, unknown_commands)
    handler = MessageHandler(Filters.all, message_handler)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(love_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(unknown_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
