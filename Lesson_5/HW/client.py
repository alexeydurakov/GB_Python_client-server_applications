import argparse
import pickle
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
import Config
import logger.client_config_for_log


# формируем сообщение
def send_msg():
    msg_to_serever = {
        "action": Config.ACTION,
        "time": Config.UNIX_TIME,
        "user": {
            "account": Config.ACCOUNT,
            "password": Config.CONTENT
        }
    }
    logger.info(f'Сформировано сообщение для пользователя {Config.ACCOUNT}')
    return msg_to_serever


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', nargs='?', type=int, default=7777)  # порт для работы
    parser.add_argument('-a', '--addr', nargs='?', default='localhost')  # адрес прослушивания
    return parser


# отправляем сообщение
def resive_msg(sock, m):
    try:
        msg = pickle.dumps(m)
        s.send(msg)
        logger.info("Сообщение отослано успешно")
    except:
        logger.error("Сообщение не отослано")
        sys.exit(1)


# получаем сообщение от сервера
def answer_msg(data):
    try:
        logger.info('Сообщение от сервера: \n', pickle.loads(data))
    except:
        logger.error("Сообщение не получено")
        sys.exit(1)


# соединение с сервером
def connect_with_sever(sock, adrr, port):
    try:
        sock.connect((adrr, port))
        logger.info(f'Соединение с сервером {host_address.addr}:{host_address.port} - успешно')
    except:
        logger.error(f'Соединение с сервером {host_address.addr}:{host_address.port} - не успешно')
        sys.exit(1)


parser = create_parser()
host_address = parser.parse_args(argv[1:])
link_adrr = host_address.addr
link_port = host_address.port

try:
    if not 1024 <= link_port <= 65535:
        logger.info(f'Порт для соединения: {link_port}')
except ValueError:
    logger.error("Порт должен быть в диапазоне 1024-6535")
    sys.exit(1)

s = socket(AF_INET, SOCK_STREAM)
logger.info(f'Идет соединение с сервером {link_adrr}":"{link_port}')
connect_with_sever(s, link_adrr, link_port)

logger.info(f'Отправка сообщения на сервер {link_adrr}":"{link_port}')
msg_to_server = send_msg()
resive_msg(s, msg_to_server)

logger.info("Получение ответа от сервера")
data = s.recv(1000000)
answer_msg(data)
s.close()

if __name__ == "__main__":
    logger = client_log_config.get_logger(__name__)
