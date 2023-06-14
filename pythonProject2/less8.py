# from tkinter import *
#
# win = Tk()
# win.title('Кликер')
# win.geometry('500x500+200+200')
#
# count = 0
#
#
# def score():
#     global count
#     count += 1
#     lab['text'] = count
#
#
# lab=Label(win,text= 'Пока нажатий не было', bg='#FF6666', fg='gold', font='10')
# lab.place(x=100,y=100)
#
# but = Button(text='Нажми на меня', bg='cyan', fg='black', font='18', command=score)
# but.place(x=150,y=200)
#
# win.mainloop()


from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

wind = Tk()
wind.geometry('500x400')
wind.title('ЦБР')

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

today = datetime.today()
today = today.strftime('%d/%m/%Y')
date= {'date': today}

response = requests.get(url, params=date)
xml = BeautifulSoup(response.content, features='html.parser')


def get_course(id):
    return xml.find('valute', {'id': id}).value.text


def get_charcode(id):
    return xml.find('valute', {'id': id}).charcode.text


def get_name(id):
    return xml.find('valute', {'id': id}).name.text


img_logo = PhotoImage(file='logo.png')
logo=Label(wind, image=img_logo)
logo.place(x=0,y=0)
lab= Label(wind,text='Курс валют \n MAXIMUM Банка', fg='black', font='Arial 22')
lab.place(y=25,x=160)
usd_course = Label(wind, text=get_charcode('R01235')+ ''+ get_name('R01235') + get_course('R01235')+ 'RUB',font='Arial 16')
usd_course.place(y=190,x=100)
eur_course = Label(wind, text='€= '+ get_course('R01239')+ 'RUB',font='Arial 16')
eur_course.place(y=230,x=100)
date_info = Label(wind, text='Курс на: '+ today.replace('/','.'), font='Arial 18')
date_info.place(y=150,x=100)
wind.mainloop()
