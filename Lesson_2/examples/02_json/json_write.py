# Запись в JSON-файлы
# Для записи в JSON-файлы на Python 3 есть два метода: dump и dumps. Первый сохраняет python-объект в json-файл.
# Второй возвращает строку в json-формате. Пример ниже демонстрирует конвертацию python-объекта в формат JSON
# (файл examples/02_json/json_write.py). Метод dumps можно применять в тех случаях, когда требуется вернуть строку в
# JSON-формате — например, для последующей ее передачи в API.

import json

dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

with open('mes_example_write.json', 'w') as f_n:
    f_n.write(json.dumps(dict_to_json))

with open('mes_example_write.json') as f_n:
    print(f_n.read())


# Чтобы записать информацию в JSON-формате в файл, корректнее применять метод dump (файл json_write.py).
import json

dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

with open('mes_example_write_2.json', 'w') as f_n:
    json.dump(dict_to_json, f_n)

with open('mes_example_write_2.json') as f_n:
    print(f_n.read())

# Определение дополнительных параметров методов записи
# Форматом вывода данных можно управлять, определив для методов записи dump и dumps дополнительные параметры.
# По умолчанию эти методы используются без них и обеспечивают запись информации в компактном представлении.
# Такой подход эффективен, когда данные используются другими приложениями, а визуальное представление — не на
# первом месте по важности. Если же предполагается, что работать с данными будет человек, а не программа, следует
# позаботиться о более удобном формате представления (json_write.py).

dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

with open('mes_example_write_3.json', 'w') as f_n:
    json.dump(dict_to_json, f_n, sort_keys=True, indent=2)

with open('mes_example_write_3.json') as f_n:
    print(f_n.read())


# В данном случае параметры sort_keys и indent позволяют выполнить сортировку данных при записи, а также установить
# величину отступа. При этом содержимое файла mes_example_write_3.json будет выглядеть следующим образом:
# {
#   "action": "msg",
#   "encoding": "ascii",
#   "from": "account_name",
#   "message": "message",
#   "to": "account_name"
# }

