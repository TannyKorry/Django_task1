import csv
from pprint import pprint

with open('data-398-2018-08-30.csv', newline='', encoding='utf8') as f:
    stantions,s = {},[]
    f_reader = csv.DictReader(f)
    stantion = []
    for row in f_reader:
        # stantions['Name'] = row.get('Name')
        # stantions['Street'] = row.get('Street')
        # stantions['District'] = row.get('District')
        stantion.append({'Name':row.get('Name'), 'Street': row.get('Street'), 'District': row.get('District')})
    # stantion.append(stantions)
    pprint(stantion)
    # pprint(s)
#
# users = []
#
# # Создание 5 новых пользователей
# for user_number in range(5):
#     # Создаём словарь для нового пользователя
#     new_user = {'age': '30', 'sex': 'Man', 'city': 'Ekaterinburg'}
#
#     # Добавляем нового пользователя в список
#     users.append(new_user)
# print(users)
# # Выводим все словари пользователей на экран
# # for user in users[:]:
#     print(user)