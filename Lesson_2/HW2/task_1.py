# Задание на закрепление знаний по модулю CSV.
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и
# формирующий новый «отчетный» файл в формате CSV.
# Для этого:
# Создать функцию get_data(),
# в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка —
# например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для
# хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде
# списка и поместить в файл main_data (также для каждого файла);

# Создать функцию write_to_csv(),
# в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;

# Проверить работу программы через вызов функции write_to_csv().
import csv
import re


def get_data():
    main_data = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    headers_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for i in [1, 2, 3]:
        with open('info_' + str(i) + '.txt', encoding='cp1251') as f:
            f_reader = csv.reader(f)
            for row in f_reader:
                param = re.split(":\s+", str(row).replace("'", '').strip('[]'))
                if headers_data[0] in param[0]:
                    os_prod_list.append(param[1])
                elif headers_data[1] in param[0]:
                    os_name_list.append(param[1])
                elif headers_data[2] in param[0]:
                    os_code_list.append(param[1])
                elif headers_data[3] in param[0]:
                    os_type_list.append(param[1])

    main_data.append(headers_data)
    main_data.append(os_prod_list)
    main_data.append(os_name_list)
    main_data.append(os_code_list)
    main_data.append(os_type_list)

    return main_data


def write_to_csv(file_csv):
    data_csv = get_data()
    print(data_csv)
    with open(file_csv, 'w') as f:
        f_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in data_csv:
            f_writer.writerow(row)



if __name__ == '__main__':
    write_to_csv('main_data.csv')