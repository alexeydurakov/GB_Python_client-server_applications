import argparse
import pickle
import select
import sys
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv

import Config
from Lesson_7.HW.log_decorator import log
from Lesson_7.HW.log_dir import server_config_for_log


@log
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', nargs='?', type=int, default=7777)  # порт для работы
    parser.add_argument('-a', '--addr', nargs='?', default='localhost')  # адрес прослушивания
    return parser


@log
def read_requests(r_clients, all_clients):
    """ Чтение запросов из списка клиентов
   """
    responses = {}  # Словарь ответов сервера вида {сокет: запрос}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            logger.info('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return responses


def write_responses(requests, all_clients):
    """ Эхо-ответ сервера клиентам, от которых были запросы
   """

    for sock in all_clients:
        for item in requests.values():
            try:
                sock.send(pickle.dumps(create_answer_msg(item['from'], item['message'])))
            except:  # Сокет недоступен, клиент отключился
                logger.info('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


@log
def create_answer_msg(frm, msg):
    msg_to_client = {
        "response": Config.STATUS_RESPONCE,
        "content": Config.CONTENT,
        "from": frm,
        "message": msg
    }
    logger.info('Сформировано сообщение')
    return msg_to_client


@log
def mainloop(link_adrr, link_port):
    """ Основной цикл обработки запросов клиентов
       """
    clients = []

    logger.info("Создание сокета")
    sock = socket(AF_INET, SOCK_STREAM)

    try:
        if not 1024 <= link_port <= 65535:
            logger.info(f'Порт для соединения: {link_port}')
    except ValueError:
        logger.error("Порт должен быть в диапазоне 1024-6535")
        sys.exit(1)
    else:
        logger.info(f'Присваивание {link_adrr}:{link_port}')
        sock.bind((link_adrr, link_port))
        logger.info("Переход в режим ожидания запросов")
        sock.listen(5)
        sock.settimeout(0.2)
        logger.info(f"Сервер запущен: {link_adrr}:{link_port}")

    while True:
        try:
            conn, addr = sock.accept()
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 10
            r = []
            w = []
            e = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass  # Ничего не делать, если какой-то клиент отключился

            requests = read_requests(r, clients)  # Сохраним запросы клиентов
            if requests:
                write_responses(requests, w, clients)  # Выполним отправку ответов клиентам

        # resive_msg(data, addr)
        #
        # send_msg()


if __name__ == '__main__':
    logger = server_config_for_log.get_logger(__name__)
    parser = create_parser()
    host_address = parser.parse_args(argv[1:])
    link_adrr = host_address.addr
    link_port = host_address.port
    mainloop(link_adrr, link_port)
