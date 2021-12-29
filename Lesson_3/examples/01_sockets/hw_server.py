# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import time
import sys
import argparse
import pickle

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p', '--port', nargs='?', type=int, default=7777)# порт для работы
    parser.add_argument ('-a', '--addr', nargs='?', default='')# адрес прослушивания
    return parser

def upload_message(data):#обрабатываем сообещние от пользователя
    print(pickle.loads(data))
    send_message()

def response():# ответ пользователю
    response = {
        "response": 200,
        "alert":"Необязательное сообщение/уведомление"
    }
    return response

def form_mes(respons):#формируем ответ пользователю
    mc = pickle.dumps(respons)
    return mc

def send_message():#отправляем сообещнеи пользователю
    respons = response()
    a = form_mes(respons)
    client.send(a)
    client.close()

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

s.bind((namespace.addr, namespace.port))# Присваивает порт
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # Одновременно обслуживает не более
                                  # 5 запросов.

while True:
    client, addr = s.accept()
    data = client.recv(1024)
    upload_message(data)