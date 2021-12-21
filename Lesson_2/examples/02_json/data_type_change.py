
import json

tuple_ex = (
       "action",
       "to",
       "from",
       "encoding",
       "message"
       )

print(type(tuple_ex))
# Out[5]:  <class 'tuple'>

with open('tuple_ex.json', 'w') as f_n:
           json.dump(tuple_ex, f_n, sort_keys=True, indent=2)

obj = json.load(open('tuple_ex.json'))

print(type(obj))
# Out[8]:  <class 'list'>

# Эта ситуация возникает из-за различия типов данных JSON и Python, поскольку не для всех из них существуют
# соответствия. Ниже приведены таблицы, описывающие типы данных при конвертации из Python в JSON и в
# обратном направлении.
# Python -> JSON:
# Python          JSON
# dict            object
# list, tuple     array
# str             string
# int, float      number
# True            true
# False           false
# None            null

# JSON -> Python:
# JSON                Python
# object              dict
# array               list
# string              str
# number (int)        int
# number (real)       float
# true                True
# false               False

# Ограничения на тип данных
# При использовании формата JSON есть ограничение: в нем нельзя сохранить словарь,
# где в качестве ключей — кортежи (data_type_change.py).
dict_to_json = {('action', 'to'): 'msg', 'from': 'account_name'}

with open('dict_to_json.json', 'w') as f_n:
            json.dump(dict_to_json, f_n)
# ...
# TypeError: key ('action', 'to') is not a string


# Использование дополнительного параметра 'skipkeys' = True позволяет игнорировать такие ключи и избегать
# ошибок (data_type_change.py).
with open('dict_to_json.json', 'w') as f_n:
            json.dump(dict_to_json, f_n, skipkeys=True)

with open('dict_to_json.json') as f_n:
            f_n_content = f_n.read()
            obj = json.loads(f_n_content)
print(obj)
# Out[13]: {'from': 'account_name'}

#
# Ключами в словарях в JSON-формате могут быть только строковые величины. Если у Python-словаря ключи определены
# в виде чисел, они будут преобразованы в строковое представление (data_type_change.py) без ошибок.

d = {5:300, 1:400}

d_to_json = json.dumps(d)

print(d_to_json)
# Out[16]: {"1": 400, "5": 300}



