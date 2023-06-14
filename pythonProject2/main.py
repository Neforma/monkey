# import telebot
# import requests
# import random
# from bs4 import BeautifulSoup
#
# token = '5557724257:AAGuc_d1yrG4TrgUQiomFV_5foY3yWuhHHc'
# bot = telebot.TeleBot(token)
#
#
# @bot.message_handler(commands=['/start'])
# def send_wel(message):
#     wel_text = 'Добро пожаловать, я Мисти Бот.'
#     bot.send_message(message.chat.id, wel_text)
#
#
# @bot.message_handler(commands=['/fact'])
# def send_fact(message):
#     response = requests.get('http://i-fakt.ru/').content
#     html = BeautifulSoup(response, 'html.parser')
#     fact = random.choice(html.find_all(class_='p-2 clearfix'))
#     fact_link = fact.a.attrs['href']
#     bot.send_message(message.chat.id, fact_link)
#
#
# bot.polling()

# def my_decorator(func_to_decorate):
#     print('Я начинаю работать')
#     func_to_decorate()
#     print('Я заканчиваю работать')
#
#
# @my_decorator
# def my_func():
#     print('Я работаю')
#
#
# my_func()
