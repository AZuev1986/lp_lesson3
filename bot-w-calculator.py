# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

DICT_S = {
    'ноль': 0,
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'умножить': '*',
    'поделить': '/',
    'плюс': '+',
    'минус': '-',
    'и': '.'
}
TEXT1 = 'похоже, что вы ввели данные в неверном формате, попробуйте еще раз, формат - "сколько будет четыре умножить на шесть" или "сколько будет четыре и пять умножить на шесть и два"'
TEXT2 = 'введите математическое выражение в формате "сколько будет четыре умножить на шесть" или "сколько будет четыре и пять умножить на шесть и два"'

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
    N = len(parts_list)
    print(N)
    for i in range(N):
        try:
            parts_list[i] = str(DICT_S[parts_list[i]])
        except KeyError:
            return update.message.reply_text(TEXT1)
    print(parts_list)
    res_string = ''.join(parts_list)
    print(res_string)
    sep = ''
    for i in range(N):
        if res_string[i] == '*' or res_string[i] == '+'or res_string[i] == '-'or res_string[i] == '/':
            sep = res_string[i]
            break
    print(sep)
    res_list = res_string.split(sep)
    print(res_list)
    try:
        arg1 = float(res_list[0])
        arg2 = float(res_list[1])
    except (ValueError, TypeError):
        return update.message.reply_text(TEXT1)
    if sep == "*":
        multiplication = arg1 * arg2
        print(multiplication)
        update.message.reply_text(round(multiplication, 3))
    elif sep == "/":
        try:
            division = arg1 / arg2
            print(division)
            update.message.reply_text(round(division, 3))
        except ZeroDivisionError:
            update.message.reply_text('похоже, что вы что-то попутали на 0 не делят')
    elif sep == "+":
        addition = arg1 + arg2
        print(addition)
        update.message.reply_text(round(addition, 3))
    elif sep == "-":   
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
