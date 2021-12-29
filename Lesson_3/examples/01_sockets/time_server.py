# Рассмотрим, как протокол TCP применяется клиентом и сервером посредством модуля socket.
#
# В этом примере сервер просто возвращает клиенту текущее время в виде строки (файл examples/01_sockets/time_server.py):

# Программа сервера времени
from socket import socket, AF_INET, SOCK_STREAM
import time

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('', 8888))                # Присваивает порт 8888
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # одновременно обслуживает не более
                                  # 5 запросов.
while True:
    client, addr = s.accept()     # Принять запрос на соединение
    print("Получен запрос на соединение от %s" % str(addr))
    timestr = time.ctime(time.time()) + "\n"
    client.send(timestr.encode('utf-8'))
    client.close()


# Вызов функции socket() запускает создание сокета. Основные параметры данной функции —
# это communication domain и type of socket. В качестве коммуникационного домена, как правило,
# передается значение AF_INET, — оно указывает, что создаваемый сокет будет сетевым.
# В качестве типа сокета указывается SOCK_STREAM — он определяет сокет как потоковый,
# то есть реализующий последовательный, надежный двусторонний поток байтов. В результате функции socket()
# создается конечная точка соединения и возвращается файловый дескриптор, который позволяет работать с сокетом,
# как с файлом — записывать и считывать данные в/из него. Таким образом, константа SOCK_STREAM указывает на то,
# что сокет работает с TCP-пакетами — то есть  это TCP-пакет.

