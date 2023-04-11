from socket import *
import os

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    if "GET" in req[0]:
        # 클라이언트가 /index.html에 접근하려는 경우
        if "/index.html" in req[0]:
            try:
                with open('HW5/index.html', 'rb') as f:
                    content = f.read()
                    c.send('HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n'.encode())
                    c.sendall(content)
            except FileNotFoundError:
                # 파일이 존재하지 않으면 404 에러 전송
                c.send('HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\n'.encode())
                c.send('404 Not Found'.encode())
        # iot.png 파일을 요청한 경우
        elif "/iot.png" in req[0]:
            try:
                with open('HW5/iot.png', 'rb') as f:
                    content = f.read()
                    c.send('HTTP/1.1 200 OK\nContent-Type: image/png\n\n'.encode())
                    c.sendall(content)
            except FileNotFoundError:
                c.send('HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\n'.encode())
                c.send('404 Not Found'.encode())
        # favicon.ico 파일을 요청한 경우
        elif "/favicon.ico" in req[0]:
            try:
                with open('HW5/favicon.ico', 'rb') as f:
                    content = f.read()
                    c.send('HTTP/1.1 200 OK\nContent-Type: image/x-icon\n\n'.encode())
                    c.sendall(content)
            except FileNotFoundError:
                c.send('HTTP/1.1 404 Not Found\n Content-Type: text/plain\n\n'.encode())
                c.send('404 Nog Found'.encode())
        else:
            c.send('HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\n'.encode())
            c.send('404 Not Found'.encode())

    else:
        c.send('HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\n'.encode())
        c.send('404 Not Found'.encode())

    c.close()
