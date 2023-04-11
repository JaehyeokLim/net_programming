from socket import *
import time

BUF_SIZE = 1024
LENGTH = 4

PORT_1 = 8888
PORT_2 = 9999

try:
    f = open('data.txt', 'r')
except:
    f = f = open('data.txt', 'w')

f.close()

while True:
    start = input("1 또는 2를 입력하세요. (종료는 quit) : ")
    if start == '1':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',PORT_1))
        s.send(b'Request')
        msg = s.recv(BUF_SIZE).decode().split()
        text = f"{time.asctime()}: Device1: Temp={msg[0]}, Humid={msg[1]}, Lilum={msg[2]}\n"
    elif start == '2':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',PORT_2))
        s.send(b'Request')
        msg = s.recv(BUF_SIZE).decode().split()
        text = f"{time.asctime()}: Device2: Heartbeat={msg[0]}, Steps={msg[1]}, Cal={msg[2]}\n"
    else:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',PORT_1))
        s.send(start.encode())
        s.recv(BUF_SIZE)
        s.close()

        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',PORT_2))
        s.send(start.encode())
        s.recv(BUF_SIZE)
        s.close()
        break
    f = open('data.txt', 'a', encoding='utf-8')
    f.write(text)
    f.close()
    s.close()
s.close()
