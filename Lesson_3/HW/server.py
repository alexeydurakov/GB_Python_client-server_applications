import argparse
import pickle
from socket import socket,  AF_INET, SOCK_STREAM
from sys import argv

msg_to_client = {
    "response": 200,
    "content": "application/json"
}
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', nargs='?', type=int, default=7777)  # порт для работы
parser.add_argument('-a', '--addr', nargs='?', default='localhost')  # адрес прослушивания
host_address = parser.parse_args(argv[1:])

s = socket(AF_INET, SOCK_STREAM)
s.bind((host_address.addr, host_address.port))
s.listen(5)

while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    print('Сообщение: \n', pickle.loads(data), '\n было отправлено клиентом: ', addr)
    msg = pickle.dumps(msg_to_client)
    client.send(msg)
    client.close()

