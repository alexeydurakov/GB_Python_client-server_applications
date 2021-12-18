
# 1 Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

items_str = ["разработка", "сокет", "декоратор"]
for item in items_str:
    print(f'Стока: {item} Тип: {type(item)}')

items_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                 '\u0441\u043e\u043a\u0435\u0442',
                 '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440',
                 ]

for item in items_unicode:
    print(f'Стока: {item} Тип: {type(item)}')

# 2 Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

item_bytes = [b'class', b'function', b'method']
for item in item_bytes:
    print(f'Стока: {item} Тип: {type(item)}')

# 3 Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
items = ['attribute', 'класс', 'функция', 'type']
for item in items:
    try:
        byte_word = bytes(item, encoding='ASCII')
        print(f'это слово возможно записать в байтовом типе {byte_word}')
    except Exception:
        print(f'это слово невозможно записать в байтовом типе "{item}"')

# 4 Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

item_worlds = ['разработка', 'администрирование', 'protocol', 'standard']
item_codes = []

for item in item_worlds:
    item_code = item.encode('utf-8')
    item_codes.append(item_code)
    print(item_code)

for item in item_codes:
    print(item.decode('utf-8'))

# 5 Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в
# строковый тип на кириллице.

import subprocess

all_ping = []
all_ping.append(['ping', 'yandex.com'])
all_ping.append(['ping', 'youtube.com'])

for item in all_ping:
    process = subprocess.Popen(item, stdout=subprocess.PIPE)
    for p in process.stdout:
        print(p.decode(encoding='cp866'))

# 6 Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его
# содержимое.

import locale

list_for_file = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as f:
    for item in list_for_file:
        f.write(item + '\n')

file_coding = locale.getpreferredencoding()

with open('test_file.txt', 'r', encoding=file_coding) as f:
    for item in f:
        print(item.replace('\n',''))

f.close()



