# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def talk_to_me(bot, update):
    update.message.reply_text('введите любую фразу в двойных кавычках в формате: /wordcount "фраза"')

def word(bot, update, args):
    user_text = update.message.text 
    print(user_text)
    list_word = user_text.split(' ')
    print(list_word)
    if list_word == ['/wordcount']:
        update.message.reply_text('похоже что вы не ввели фразу, попробуйте еще раз')
    else:
        if list_word[1][0] == '"' and list_word[-1][-1] == '"' and list_word != ['/wordcount', '"']:
            if list_word == ['/wordcount', '""']:
                print('пустая строка')
                update.message.reply_text('похоже что вы ввели пустую строку, попробуйте еще раз')
            else:
                word_c = len(list_word) - 1
                update.message.reply_text('количество слов: {}'.format(word_c))
        else:
            print('неверный формат')
            update.message.reply_text('похоже что вы ввели данные в неверном формате, попробуйте еще раз')

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY1)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('wordcount', word, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()