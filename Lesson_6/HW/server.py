import argparse
import pickle
import sys
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv

import Config
import logger.server_config_for_log
from Lesson_6.HW.log_decorator import log


@log
def answer_msg():
    msg_to_client = {
        "response": Config.STATUS_RESPONCE,
        "content": Config.CONTENT
    }
    logger.info('Сформировано сообщение')
    return msg_to_client

@log
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', nargs='?', type=int, default=7777)  # порт для работы
    parser.add_argument('-a', '--addr', nargs='?', default='localhost')  # адрес прослушивания
    return parser

@log
def resive_msg(data, addr):
    try:
        logger.info('Сообщение: \n', pickle.loads(data), '\n было отправлено клиентом: ', addr)
    except:
        logger.error(f'Сообщение от клиента {addr} не получено')
        sys.exit(1)

@log
def send_msg():
    try:
        msg_to_client = answer_msg()
        msg = pickle.dumps(msg_to_client)
        client.send(msg)
        logger.info("Сообщение клиенту отправлено успешно")
    except:
        logger.error("Сообщение клиенту не отправлено")


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

logger.info("Создание сокета")
s = socket(AF_INET, SOCK_STREAM)
logger.info(f'Присваивание {link_adrr}:{link_port}')
s.bind((link_adrr, link_port))
logger.info("Переход в режим ожидания запросов")
s.listen(5)

while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    logger.info("Получение сообщения от клиента")
    resive_msg(data, addr)
    logger.info("Отправка сообщения клиенту")
    send_msg()
    client.close()


