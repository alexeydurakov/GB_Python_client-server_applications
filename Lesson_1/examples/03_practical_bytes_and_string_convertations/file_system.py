# Работа с файловой системой
# Чтобы обратиться к определенному файлу и прочесть его содержимое, применяется следующая конструкция:
file_name = 'text.txt'
with open(file_name) as f_n:
    for el_str in f_n:
        print(el_str)

# На практике при чтении из файла извлекаются данные, которые автоматически преобразуются в строковое представление.
# При этом используется кодировка по умолчанию. Для русскоязычных версий ОС Windows это, как правило, cp1251

import locale

def_coding = locale.getpreferredencoding()

print(def_coding)
# Out[48]: cp1251

# При работе с файлами также можно определить наименование кодировки, которая будет использоваться при операциях с ними
f_n = open("test.txt", "w")

f_n.write("test test test")

f_n.close()

print(f_n)
# Out[52]:  <_io.TextIOWrapper name='test.txt' mode='w' encoding='cp1251'>

# Но при выполнении операций с файловой системой более корректная практика — явно указывать кодировку,
# поскольку она может различаться в ОС

with open('test.txt', encoding='utf-8') as f_n:

    for el_str in f_n:
        print(el_str, end='')
# Out[54]:  test test test



