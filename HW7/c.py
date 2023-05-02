# import socket
# import threading

# def handler(sock):
#     while True:
#         msg, addr = sock.recvfrom(1024) 
#         print(msg.decode())
# svr_addr = ('localhost', 2500)
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# my_id = input('ID를 입력하세요: ') 
# sock.sendto(('['+my_id+']').encode(), svr_addr)
# th = threading.Thread(target=handler, args=(sock,)) 
# th.daemon = True
# th.start()

# while True:
#     msg = '[' + my_id + '] ' + input() 
#     sock.sendto(msg.encode(), svr_addr)

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2500))

my_id = input('ID를 입력하세요: ')
s.sendall(('['+my_id+']').encode())

def receive():
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())

import threading
th = threading.Thread(target=receive)
th.daemon = True
th.start()

while True:
    msg = '[' + my_id + '] ' + input()
    s.sendall(msg.encode())
