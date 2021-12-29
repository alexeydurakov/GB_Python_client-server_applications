from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR, SO_BROADCAST

s = socket(AF_INET, SOCK_DGRAM)           # Определяем UDP-протокол
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # Несколько приложений может слушать сокет
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) # Определяем широковещательные пакеты
s.bind(('', 8888))
while True:
	msg = s.recv(128)
	print(msg.decode('utf-8'))