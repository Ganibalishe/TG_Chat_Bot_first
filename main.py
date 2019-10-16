from telegram import *
from telegram.ext import *
from config import TG_TOKEN
from config import TG_API_URL


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'Братишка'

    text = update.effective_message.text
    reply_text = f'Привет, {name}!\n\n{text}'

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

    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
