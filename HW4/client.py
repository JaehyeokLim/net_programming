import socket

HOST = 'localhost'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print('서버에 연결되었습니다.')

    while True:
        data = input('계산식을 입력하세요: ')
        if data == 'q':
            break

        client_socket.sendall(data.encode())
        result = client_socket.recv(1024).decode()
        print(f'결과: {result}')
        
    print('서버와의 연결이 종료되었습니다.')
