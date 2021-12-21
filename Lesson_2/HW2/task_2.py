# Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
# Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
# orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_json = {}

    dict_json['item'] = item
    dict_json['quantity'] = quantity
    dict_json['price'] = price
    dict_json['buyer'] = buyer
    dict_json['data'] = date

    with open('orders.json', 'w') as f:
        json.dump(dict_json, f, indent=4)


write_order_to_json('Table', 2, 1500, 'Petrov', "21.12.21")