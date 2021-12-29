import argparse
import pickle
import time
from socket import socket,  AF_INET, SOCK_STREAM
from sys import argv

msg_to_serever = {
    "action": "presense",
    "time": time.time(),
    "user": {
        "account": "account_name"
    }
}
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', nargs='?', type=int, default=7777)  # порт для работы
parser.add_argument('-a', '--addr', nargs='?', default='localhost')  # адрес прослушивания
host_address = parser.parse_args(argv[1:])

s = socket(AF_INET, SOCK_STREAM)
s.connect((host_address.addr, host_address.port))

msg = pickle.dumps(msg_to_serever)
s.send(msg)
data = s.recv(1000000)
print('Сообщение от сервера: \n', pickle.loads(data))
s.close()

