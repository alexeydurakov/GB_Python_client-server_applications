# Примеры конвертации байтов и строк

# Модуль subprocess

import subprocess

args = ['ping', 'google.com']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
#
# for line in subproc_ping.stdout:
#         print(line)
# Out[44]: b'\x8e\xa1\xac\xa5\xad \xaf\xa0\xaa\xa5\xe2\xa0\xac\xa8...'

# Чтобы обработать полученный результат, его необходимо конвертировать в строковый формат.
# При этом в цикле надо выполнить декодирование строки в байтовом выражении и перевести ее в Unicode
# for line in subproc_ping.stdout:
#             print(line.decode('utf-8'))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8e in position 0: invalid start byte

# На вычислительных устройствах под управлением русифицированной ОС Windows при запуске консольных приложений чаще
# всего используется кириллическая кодировка cp866, в которой и закодирован выводимый результат работы модуля subprocess.
# Для других приложений — это windows-1251

for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

# Out[46]: Обмен пакетами с google.com [74.125.232.224] с 32 байтами данных:
# Ответ от 74.125.232.224: число байт=32 время=36мс TTL=56
# Ответ от 74.125.232.224: число байт=32 время=36мс TTL=56
# Ответ от 74.125.232.224: число байт=32 время=36мс TTL=56
# Ответ от 74.125.232.224: число байт=32 время=36мс TTL=56
# Статистика Ping для 74.125.232.224:
#
#     Пакетов: отправлено = 4, получено = 4, потеряно = 0
#     (0% потерь)
# Приблизительное время приема-передачи в мс:
#     Минимальное = 36 мсек, Максимальное = 36 мсек, Среднее = 36 мсек

# Модуль telnetlib
# Модуль telnetlib предоставляет класс Telnet, реализующий протокол Telnet и позволяющий пользователю работать с
# удаленным компьютером, как со своим.

# Особенность модуля telnetlib — необходимость передачи данных в байтах, а не в строках при работе с методами
# read_until и write. Поскольку возвращаемый результат также представляет собой байты, надо обязательно выполнить
# декодирование

import telnetlib
import time

tn_connect = telnetlib.Telnet('10.0.0.1')

tn_connect.read_until(b'Username:')
tn_connect.write(b'user\n')

t.read_until(b'Password:')
t.write(b'pass\n')

time.sleep(5)

output = tn_connect.read_very_eager().decode('cp866').encode('utf-8')
print(output.decode('utf-8'))
