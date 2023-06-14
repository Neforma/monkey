# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
#
# today = datetime.today()
# today = today.strftime('%d/%m/%Y')
#
# url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
# date = {'date_req':today}
#
# response = requests.get(url, params=date)
# xml = BeautifulSoup(response.content, 'html.parser')
#
#
# def get_courses(id):
#     return xml.find('valute', {'id': id}).value.text
#
#
# print(get_courses('R01010'), 'За 1 австралийский доллар')
# print(get_courses('R01235'), 'За 1 американский доллар')

my_file = open('file.txt', 'w')
my_file.write('Максон чорт')
my_file.close()

my_file = open('file.txt', 'a')
my_file.write(' чёрный')
my_file.close()

my_file = open('file.txt', 'r')
my_text = my_file.read()
print(my_text)
my_file.close()