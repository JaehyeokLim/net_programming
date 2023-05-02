# import socket
# import time
# clients = [] # 클라이언트 목록
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('', 2500))
# print('Server Started')

# while True:
#     data, addr = s.recvfrom(1024)
#     # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제 if 'quit' in data.decode():
#     if addr in clients:
#         print(addr, 'exited')
#         clients.remove(addr)
#         continue
#     # 새로운 클라이언트이면 목록에 추가 
#     if addr not in clients:
#         print('new client', addr)
#         clients.append(addr)
#     print(time.asctime() + str(addr) + ':' + data.decode())
#     # 모든 클라이언트에게 전송 
#     for client in clients: 
#         if client != addr:
#             s.sendto(data, client)

import socket
import threading
import time

clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 2500))
s.listen()

def handler(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = f'{data.decode()}'
        print(f'{time.asctime()}(\'{addr[0]}\', {addr[1]}):{msg}')
        for client in clients:
            if client != conn:
                client.sendall(msg.encode())
    print(f'[{addr[0]}:{addr[1]}] disconnected')
    clients.remove(conn)
    conn.close()

print('Server Started')

while True:
    conn, addr = s.accept()
    clients.append(conn)
    print(f'new client (\'{addr[0]}\', {addr[1]})')
    # print(f'[{addr[0]}:{addr[1]}] connected')
    th = threading.Thread(target=handler, args=(conn, addr))
    th.daemon = True
    th.start()
