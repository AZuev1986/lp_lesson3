# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem

TEXT1 = 'похоже, что вы ввели данные в неверном формате, попробуйте еще раз, формат - "Когда ближайшее полнолуние после 2016-10-01?"'

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='moon_bot.log'
                    )

def moon(bot, update):
    user_text = str(update.message.text)
    user_text = user_text.replace('"Когда ближайшее полнолуние после ', '')
    user_text = user_text.replace('"', '')
    print(user_text)
    try:
        res_date = ephem.next_full_moon(user_text)
        print(res_date)
        update.message.reply_text('Ближайшее полнолуние будет {}'.format(res_date))
    except (ValueError, TypeError):
        update.message.reply_text(TEXT1)
    
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY1)
    dp = mybot.dispatcher
    dp.add_handler(MessageHandler(Filters.text, moon))
    mybot.start_polling()
    mybot.idle()

main()
