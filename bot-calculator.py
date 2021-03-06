# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot-calculator.log'
                    )

def calculator(bot, update):

    user_text = update.message.text 
    print(user_text)
    if user_text[0] == '"' and user_text[-1] == '"' and user_text[-2] == '=':
        standard_text = user_text[1:-2]
        print(standard_text)
        act = "*/+-"
        for i in act:
            parts = standard_text.split(i)
            try:
                arg1 = float(parts[0])
                arg1 = float(parts[1])
            except (ValueError, TypeError):
                update.message.reply_text('похоже, что вы ввели данные в неверном формате, попробуйте еще раз')
                break
            if len(parts) == 2:
                if i == "*":
                    multiplication = arg1 * arg2
                    print(multiplication)
                    update.message.reply_text(round(multiplication, 3))
                elif i == "/":
                    try:
                        division = arg1 / arg2
                        print(division)
                        update.message.reply_text(round(division, 3))
                    except ZeroDivisionError:
                        update.message.reply_text('похоже, что вы что-то попутали на 0 не делят')
                elif i == "+":
                    addition = arg1 + arg2
                    print(addition)
                    update.message.reply_text(round(addition, 3))
                elif i == "-":
                    difference = arg1 - arg2
                    print(difference)
                    update.message.reply_text(round(difference,3))
                break
            elif len(parts) > 2:
                update.message.reply_text('триал версия калькулятора работает только с двумя числами')
    update.message.reply_text('введите математическое выражение в формате "2*1.3="')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY1)
    dp = mybot.dispatcher
    dp.add_handler(MessageHandler(Filters.text, calculator))
    mybot.start_polling()
    mybot.idle()

main()
