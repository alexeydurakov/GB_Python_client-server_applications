
# Запись данных в файл формата CSV

import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('kp_data_write.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n)
    for row in data:
        f_n_writer.writerow(row)

with open('kp_data_write.csv') as f_n:
    print(f_n.read())

# Результат:
# hostname,vendor,model,location
#
# kp1,Cisco,2960,"Moscow, str"
#
# kp2,Cisco,2960,"Novosibirsk, str"
#
# kp3,Cisco,2960,"Kazan, str"
#
# kp4,Cisco,2960,"Tomsk, str"


# Считается хорошей практикой явное указание кавычек для каждого значения, даже если оно не содержит запятых.
# Но необязательно указывать их явно. В модуле csv можно программно определять такую опцию

data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('kp_data_write_2.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        f_n_writer.writerow(row)

with open('kp_data_write_2.csv') as f_n:
    print(f_n.read())


# Результат:
# "hostname","vendor","model","location"
#
# "kp1","Cisco","2960","Moscow, str"
#
# "kp2","Cisco","2960","Novosibirsk, str"
#
# "kp3","Cisco","2960","Kazan, str"
#
# "kp4","Cisco","2960","Tomsk, str"


# В модуле csv для итератора реализован полезный метод writerows, позволяющий не построчно записывать данные в файл,
# а передать объект (например, список) с данными в качестве аргумента и выполнить мгновенную запись сразу всех данных

data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('kp_data_write_3.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    f_n_writer.writerows(data)

with open('kp_data_write_3.csv') as f_n:
    print(f_n.read())


# Метод DictWriter позволяет сохранять словари в csv-представлении. Принцип работы этого метода и стандартного writer
# практически совпадают. Но упорядоченность реализована применительно к словарям Python только с версии 3.6,
# поэтому необходимо явно указывать порядок следования столбцов в файле. За это отвечает параметр fieldnames.
# В качестве разделителя можно определить любой символ, который устанавливается как значение параметра
# delimiter метода reader. Например, если данные в файле разделены с помощью «!», можно указать модулю csv
# использовать именно восклицательный знак при разделении данных (файл examples/01_csv/kp_data_delimiter.csv).
# hostname!vendor!model!location
# kp1!Cisco!2960!Moscow
# kp2!Cisco!2960!Novosibirsk
# kp3!Cisco!2960!Kazan
# kp4!Cisco!2960!Tomsk

#
# Простейший код с использованием разделителя (csv_write.py):
with open('kp_data_delimiter.csv') as f_n:
    f_n_reader = csv.reader(f_n, delimiter='!')
    for row in f_n_reader:
        print(row)




