# import requests
#
# url= "https://swapi.dev/api/"
#
# response = requests.get(url).json()
#
# people_api = response.get('people')
# planet_api = response.get('planets')
# starship_api = response.get('starships')
#
# # def check_people(url):
# #     num = int(input('Введите номер персонажа: '))
# #     response = requests.get(f'{url}/{num}').json()
# #     print(response)
#
#
# def check_people(url):
#     for num in range(1,6):
#         response = requests.get(f'{url}/{num}').json()
#         print(response)
#
#
# def check_planet(url):
#     diameters_planet = []
#     for i in range(1,6):
#         response = requests.get(f'{url}/{i}').json()
#         diameters_planet.append({response.get('name'): response.get('diameter')})
#     print(diameters_planet)
#
#
# def check_starship(url):
#     diameters_planet = []
#     for i in range(1,6):
#         response = requests.get(f'{url}/{i}').json()
#         print(response)
#
# # check_people(people_api)
# # check_planet(planet_api)
# check_starship(starship_api)


# var_1 = True
# var_2 = False
# var_3 = 5 > 1
# print(var_3)
# print(type(var_1))
#
# if var_1 == False:
#     pass
# else:
#     print('Условие не выполнено')

# time = int(input('Введите текущий час: '))
# if 17 >= time >= 12:
#     print('День')
# elif time >= 17 and time <= 23:
#     print('Вечер')

# a = int(input('Первое число:'))
# b = int(input('Второе число: '))
# c = int(input('Третье число: '))
#
# if a > b and a > c:
#     print('Наибольшее: ', a)
# elif b > a and b > c:
#     print('Наибольшее: ', b)
# elif c > a and c > b:
#     print('Наибольшее: ', c)
# if a < b and a < c:
#     print('Наименьшее: ', a)
# elif b < a and b < c:
#     print('Наименьшее: ', b)
# elif c < a and c < b:
#     print('Наименьшее: ', c)

a = int(input('Погода вчера: '))
b = int(input('Погода сегодня: '))
c = int(input('Погода завтра: '))
if a > b and a > c:
    print('Вчера было теплее, чем сегодня и завтра')
elif a > b and a < c:
    print('Вчера было теплее, чем сегодня, но холоднее, чем завтра')
elif a < b and a > c:
    print('Вчера было холоднее, чем сегодня, но теплее, чем завтра')
elif a < b and a < c:
    print('Вчера было холоднее, чем сегодня и завтра')

elif b > a and b > c:
    print('Сегодня теплее, чем вчера и завтра')
elif b > a and b < c:
    print('Сегодня теплее, чем вчера, но холоднее, чем завтра')
elif b < a and b > c:
    print('Сегодня холоднее, чем вчера, но теплее, чем завтра')
elif b < a and b < c:
    print('Сегодня холоднее, чем вчера и завтра')

elif c > a and c > b:
    print('Завтра будет теплее, чем сегодня и вчера')
elif c > a and c < b:
    print('Завтра будет теплее, чем вчера, но холоднее, чем сегодня')
elif c < a and c > b:
    print('Завтра будет холоднее, чем вчера, но теплее, чем сегодня')
elif c < a and c < b:
    print('Завтра будет холоднее, чем вчера и сегодня')