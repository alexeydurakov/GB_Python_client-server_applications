
# Чтение данных из файла формата CSV

import csv
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    for row in f_n_reader:
        print(row)

# Результат выполнения этого кода:
# ['hostname', 'vendor', 'model', 'location']
# ['kp1', 'Cisco', '2960', 'Moscow']
# ['kp2', 'Cisco', '2960', 'Novosibirsk']
# ['kp3', 'Cisco', '2960', 'Kazan']
# ['kp4', 'Cisco', '2960', 'Tomsk']

# В фрагменте csv_read.py обратим внимание на модуль csv.reader, который принимает в качестве параметра ссылку на объект,
# поддерживающий протокол итератора. Значением параметра может быть любой объект, для которого доступен метод write().
# При этом в переменной f_n_reader содержится указатель на сам итератор:
with open('kp_data.csv') as f_n:
           f_n_reader = csv.reader(f_n)
           print(f_n_reader)
# Out[1]: <_csv.reader object at 0x0000000003116048>


# Полученный итератор также можно преобразовать в список (csv_read.py):
with open('kp_data.csv') as f_n:
           f_n_reader = csv.reader(f_n)
           print(list(f_n_reader))
# Out[2]:  [['hostname', 'vendor', 'model', 'location'],
#           ['kp1', 'Cisco', '2960', 'Moscow'],
#           ['kp2', 'Cisco', '2960', 'Novosibirsk'],
#           ['kp3', 'Cisco', '2960', 'Kazan'],
#           ['kp4', 'Cisco', '2960', 'Tomsk']]

# На практике может потребоваться отделить строки с заголовками от содержимого таблицы при выводе.
# Для этого можно применить следующий алгоритм (csv_read.py):
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    f_n_headers = next(f_n_reader)
    print('Headers: ', f_n_headers)
    for row in f_n_reader:
        print(row)


# Результат:
# Headers:  ['hostname', 'vendor', 'model', 'location']
# ['kp1', 'Cisco', '2960', 'Moscow']
# ['kp2', 'Cisco', '2960', 'Novosibirsk']
# ['kp3', 'Cisco', '2960', 'Kazan']
# ['kp4', 'Cisco', '2960', 'Tomsk']

# Еще один вариант чтения данных из файла предлагает метод DictReader модуля csv. Он реализует более удобный и
# понятный формат вывода, когда каждой строке таблицы соответствует словарь, в котором элементы представляют
# собой связку «ключ (название столбца): значение (значение столбца)» (csv_read.py):
with open('kp_data.csv') as f_n:
    f_n_reader = csv.DictReader(f_n)
    for row in f_n_reader:
        print(row)
# Можно выводить содержимое отдельных столбцов.При этом необходимо указать их ключи - названия(csv_read.py):
        print(row['hostname'], row['model'])

#
# Результат:
# {'hostname': 'kp1', 'vendor': 'Cisco', 'model': '2960', 'location': 'Moscow'}
# {'hostname': 'kp2', 'vendor': 'Cisco', 'model': '2960', 'location': 'Novosibirsk'}
# {'hostname': 'kp3', 'vendor': 'Cisco', 'model': '2960', 'location': 'Kazan'}
# {'hostname': 'kp4', 'vendor': 'Cisco', 'model': '2960', 'location': 'Tomsk'}
# Результат:
# kp1 2960
# kp2 2960
# kp3 2960
# kp4 2960













