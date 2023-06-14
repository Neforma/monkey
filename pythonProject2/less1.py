# num = 5
# string = 'Привет'
# print(type(num), type(string))
# print("{1}, {0} Seva".format(string, num))
# text = 'Привет, мир!'
# sub_string_hello = text[0:6]
# sub_string_1 = text[8:11]
# print(sub_string_hello)
# print(sub_string_1)

# try:
#     number_1 = int(input())
#     number_2 = int(input())
# except ValueError:
#     print('Неправильный формат числа')
# else:
#     if number_1 > number_2:
#         print(number_1-number_2)
#     elif number_1 < number_2:
#         print(number_1 + number_2)
#     else:
#         print(number_1*number_2)

# for i in range(1000, -8, -7):
#     print(i)

# def add(x,y):
#     return x+y
#
#
# print(add(1,22))
#
#
# def hello():
#     name = input('Как вас зовут? ')
#     print('Приятно познакомиться ' + name)
# hello()

import math


def calculate():
    print('* - умножение')
    print('/ - деление')
    print('+ - сложение')
    print('- - вычитание')
    print('D - Дискриминант')
    print('S - Корень')
    type1 = input('Выберите операцию: ')

    if type1 == '+':
        a = input('Введите первое число: ')
        b = input('Введите второе число: ')
        try:
            res = int(a) + int(b)
        except ValueError:
            print('Неизвестные значения')
        else:
            print(res)
        print('-' * 20)
        calculate()
    elif type1 == '-':
        a = input('Введите первое число: ')
        b = input('Введите второе число: ')
        try:
            res = int(a) - int(b)
        except ValueError:
            print('Неизвестные значения')
        else:
            print(res)
        print('-' * 20)
        calculate()
    elif type1 == '*':
        a = input('Введите первое число: ')
        b = input('Введите второе число: ')
        try:
            res = int(a) * int(b)
        except ValueError:
            print('Неизвестные значения')
        else:
            print(res)
        print('-' * 20)
        calculate()
    elif type1 == '/':
        a = input('Введите первое число: ')
        b = input('Введите второе число: ')
        try:
            res = int(a) / int(b)
        except ValueError:
            print('Неизвестные значения')
        else:
            print(res)
        print('-' * 20)
        calculate()
    elif type1 == 'D':
        a = input('Введите первое число: ')
        b = input('Введите второе число: ')
        c = input('Введите третье число: ')
        try:
            res = int(b**2) - 4 * int(a) * int(c)
        except ValueError:
            print('Неизвестные значения')
        else:
            print(res)
        print('-' * 20)
        calculate()
    elif type1 == 'S':
        a = input('Введите число: ')
        try:
            res = math.sqrt(int(a))
        except ValueError:
            print('Неизвестные значения')
        else:
            print(res)
        print('-' * 20)
        calculate()
    else:
        print('Операция неизвестна, повторите ввод')
        calculate()


calculate()