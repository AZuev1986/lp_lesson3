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
ACTION = {
    'умножить': '*',
    'поделить': '/',
    'плюс': '+',
    'минус': '-'
}
TEXT1 = 'похоже, что вы ввели данные в неверном формате, попробуйте еще раз, формат - "сколько будет три минус два" или "сколько будет четыре умножить на шесть"'
TEXT2 = 'введите математическое выражение в формате "сколько будет три минус два" или "сколько будет четыре умножить на шесть"'

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot-w-calculator.log'
                    )

def calculator(bot, update):
    user_text = str(update.message.text)
    user_text = user_text.replace('"сколько будет ', '')
    user_text = user_text.replace('"', '')
    user_text = user_text.replace('на ', '')
    print (user_text)
    parts_list = user_text.split()
    print(parts_list)
    try:
        parts_list[0] = DICT_NUMBER[parts_list[0]]
        parts_list[1] = ACTION[parts_list[1]]
        parts_list[2] = DICT_NUMBER[parts_list[2]]
    except (KeyError, IndexError):
        return update.message.reply_text(TEXT1)
    print(parts_list)
    try:
        arg1 = int(parts_list[0])
        arg2 = int(parts_list[2])
    except (ValueError, TypeError):
        return update.message.reply_text(TEXT1)
    if parts_list[1] == "*":
        multiplication = arg1 * arg2
        print(multiplication)
        update.message.reply_text(round(multiplication, 3))
    elif parts_list[1] == "/":
        try:
            division = arg1 / arg2
            print(division)
            update.message.reply_text(round(division, 3))
        except ZeroDivisionError:
            update.message.reply_text('похоже, что вы что-то попутали на 0 не делят')
    elif parts_list[1] == "+":
        addition = arg1 + arg2
        print(addition)
        update.message.reply_text(round(addition, 3))
    elif parts_list[1] == "-":   
        difference = arg1 - arg2
        print(difference)
        update.message.reply_text(round(difference,3))
    update.message.reply_text(TEXT2)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY1)
    dp = mybot.dispatcher
    dp.add_handler(MessageHandler(Filters.text, calculator))
    mybot.start_polling()
    mybot.idle()

main()
