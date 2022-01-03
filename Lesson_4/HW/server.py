import argparse
import pickle
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
import Config


def answer_msg():
    msg_to_client = {
        "response": Config.STATUS_RESPONCE,
        "content": Config.CONTENT
    }
    return msg_to_client


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', nargs='?', type=int, default=7777)  # порт для работы
    parser.add_argument('-a', '--addr', nargs='?', default='localhost')  # адрес прослушивания
    return parser


def resive_msg(data, addr):
    print('Сообщение: \n', pickle.loads(data), '\n было отправлено клиентом: ', addr)


def send_msg():
    msg_to_client = answer_msg()
    msg = pickle.dumps(msg_to_client)
    client.send(msg)



parser = create_parser()
host_address = parser.parse_args(argv[1:])

s = socket(AF_INET, SOCK_STREAM)
s.bind((host_address.addr, host_address.port))
s.listen(5)

while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    resive_msg(data, addr)
    send_msg()
    client.close()
