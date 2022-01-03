import argparse
import pickle
import time
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
import Config

def send_msg():
    msg_to_serever = {
        "action": Config.ACTION,
        "time": Config.UNIX_TIME,
        "user": {
            "account": Config.ACCOUNT,
            "password": Config.CONTENT
        }
    }
    return msg_to_serever


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', nargs='?', type=int, default=7777)  # порт для работы
    parser.add_argument('-a', '--addr', nargs='?', default='localhost')  # адрес прослушивания
    return parser

def resive_msg(m):
    msg = pickle.dumps(m)
    return msg

def answer_msg(data):
    print('Сообщение от сервера: \n', pickle.loads(data))

parser = create_parser()
host_address = parser.parse_args(argv[1:])

s = socket(AF_INET, SOCK_STREAM)
s.connect((host_address.addr, host_address.port))

msg_to_server = send_msg()
s.send(resive_msg(msg_to_server))
data = s.recv(1000000)
answer_msg(data)
s.close()
