# Для операций с JSON-объектами в Python 3 предназначен модуль json, в котором для чтения данных реализовано два метода:
# load и loads. Первый считывает файл в JSON-формате и возвращает python-объекты. Второй — отвечает за считывание
# строки в JSON-формате и тоже возвращает python-объекты (файл examples/02_json/json_read.py). Пример использования
# метода load:
import json

with open('msg_example_read.json') as f_n:
    objs = json.load(f_n)

print(objs)

for section, commands in objs.items():
    print("Section: " + section)
    print("Commands: " + commands)

print('-' * 50)
# Результат выполнения данного кода:
# action
# msg
# from
# account_name
# to
# account_name
# encoding
# ascii
# message
# message


# Пример использования метода loads с аналогичным предыдущему примеру результатом (файл examples/02_json/json_read.py):
with open('msg_example_read.json') as f_n:
    f_n_content = f_n.read()
    objs = json.loads(f_n_content)

print(objs)

for section, commands in objs.items():
    print("Section: " + section)
    print("Commands: " + commands)

    

