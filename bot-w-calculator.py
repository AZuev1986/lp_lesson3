# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

DICT_NUMBER = {
    'ноль': 0,
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9
}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot-w-calculator.log'
                    )

def calculator(bot, update):
    user_text = str(update.message.text)
    user_text = user_text.replace('сколько будет', '1')
    print (user_text)
    if user_text[0] == '"' and user_text[-1] == '"' and user_text[1] == 'сколько' and user_text[2] == 'будет':
        standard_text = user_text[1:-2]
        print(standard_text)
        act = [' умножить ', ' поделить ', ' плюс ', ' минус ']
        for i in act:
            parts = standard_text.split(i)
            try:
                arg1 = float(DICT_NUMBER[parts[0]])
                arg1 = float(DICT_NUMBER[parts[0]])
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
    update.message.reply_text('введите математическое выражение в формате "сколько будет три минус два" или "сколько будет четыре умножить на шесть"')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY1)
    dp = mybot.dispatcher
    dp.add_handler(MessageHandler(Filters.text, calculator))
    mybot.start_polling()
    mybot.idle()

main()
