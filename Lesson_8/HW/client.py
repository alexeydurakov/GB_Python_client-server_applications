import argparse
import pickle
import sys
import threading
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
from Lesson_7.HW.log_decorator import log
from Lesson_7.HW.log_dir import client_config_for_log


@log
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', nargs='?', type=int, default=7777)  # порт для работы
    parser.add_argument('-a', '--addr', nargs='?', default='localhost')  # адрес прослушивания
    return parser


@log
def resive_msg(sock, adrr, port):
    while True:
        msg = input('Сообщение: ')
        if msg == 'exit' or msg == 'quit':
            sys.exit(1)
        try:
            msg = pickle.dumps(m)
            sock.send(msg.encode('utf-8'))
            print(f'Сообщение по адресу {adrr}:{port} отослано успешно')
            logger.info(f'Сообщение по адресу {adrr}:{port} отослано успешно')
        except:
            print(f'Сообщение по адресу {adrr}:{port} не отослано')
            logger.error(f'Сообщение по адресу {adrr}:{port} не отослано')
            sys.exit(1)


def loads_msg(sock, adrr, port):
    while True:
        try:
            data = sock.recv(1024)
            if isinstance(data, bytes):
                response = pickle.loads(data)

                if isinstance(response, dict):
                    print(f'\nПолучено сообщение от {adrr}:{port} - \n{response["message"]}')
                    logger.info(f'Получено сообщение от {adrr}:{port} - \n{response["message"]}')

                else:
                    print(f'Получено некорректное сообщение от {adrr}:{port}')
                    logger.error(f'Получено некорректное сообщение от {adrr}:{port}')
        except:
            logger.error(f'Не удалось декодировать полученное сообщение.')
            print(f'Не удалось декодировать полученное сообщение.')
            break

@log
def connect_with_sever(sock, adrr, port):
    try:
        sock.connect((adrr, port))
        logger.info(f'Соединение с сервером {host_address.addr}:{host_address.port} - успешно')
    except:
        logger.error(f'Соединение с сервером {host_address.addr}:{host_address.port} - не успешно')
        sys.exit(1)


def echo_client(link_adrr, link_port):
    try:
        if not 1024 <= link_port <= 65535:
            logger.info(f'Порт для соединения: {link_port}')
    except ValueError:
        logger.error("Порт должен быть в диапазоне 1024-6535")
        sys.exit(1)
    else:
        with socket(AF_INET, SOCK_STREAM) as sock:  # Создать сокет TCP
            try:
                logger.info(f'Идет соединение с сервером {link_adrr}:{link_port}')
                connect_with_sever(sock, link_adrr, link_port)
            except:
                logger.error("Cоединение с сервером не установлено")
                sys.exit(1)
            else:
                #приём сообщний
                receiver = threading.Thread(target=loads_msg, args=(sock, link_adrr, link_port))
                receiver.daemon = True
                receiver.start()

                #отправка сообщений
                user_interface = threading.Thread(target=resive_msg, args=(sock, link_adrr, link_port))
                user_interface.daemon = True
                user_interface.start()
                logger.debug('Запущены процессы')


if __name__ == "__main__":
    logger = client_config_for_log.get_logger(__name__)
    parser = create_parser()
    host_address = parser.parse_args(argv[1:])
    link_adrr = host_address.addr
    link_port = host_address.port
    echo_client(link_adrr, link_port)
