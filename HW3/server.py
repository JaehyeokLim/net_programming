import socket
s = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
s.bind(('', 8000))
s.listen(2)
while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    # 학생의 이름을 수신한 후 출력
    msg = client.recv(1024)
    print(msg.decode())

    # 학생의 학번을 전송
    student_id = 20181536
    data = student_id.to_bytes(4, byteorder='big')
    client.send(data)  
    client.close()