# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from decimal import Decimal
import logging

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot-calculator.log'
                    )

def calculator(bot, update):
    update.message.reply_text('введите математическое выражение в формате "2-3="')
    user_text = update.message.text 
    print(user_text)
    if user_text[0] == '"' and user_text[-1] == '"' and user_text[-2] == '=':
        standard_text = user_text[0:-3]
        print(standard_text)
        act = "*/+-"
        for i in act:
            parts = s.split(i)
            if len(parts) == 2:
                if i == "*":
                    multiplication = Decimal(parts[0]) * Decimal(parts[1])
                    print(multiplication)
                    update.message.reply_text(multiplication)
                elif i == "/":
                    division = Decimal(parts[0]) / Decimal(parts[1])
                    if Decimal(parts[1]) == 0:
                        update.message.reply_text('вы что-то попутали, на ноль не делят ')
                    else: 
                        print(division)
                        update.message.reply_text(division)
                elif i == "+":
                    addition = Decimal(parts[0]) + Decimal(parts[1])
                    print(addition)
                    update.message.reply_text(addition)
                elif i == "-":
                    difference = Decimal(parts[0]) - Decimal(parts[1])
                    print(difference)
                    update.message.reply_text(difference)
                break
            elif len(parts) > 2:
                raise Exception('триал версия калькулятора работает только с двумя числами')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY1)
    dp = mybot.dispatcher
    dp.add_handler(MessageHandler(Filters.text, calculator)
    mybot.start_polling()
    mybot.idle()

main()
