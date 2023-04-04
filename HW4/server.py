import socket

def calculate(expression):
    # 입력 받은 계산식을 파싱해서 연산을 수행한 결과를 반환하는 함수
    try:
        tokens = expression.split()
        op = tokens[1]
        num1 = int(tokens[0])
        num2 = int(tokens[2])
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return round(num1 / num2, 1) # 소수점 1자리까지만 표시
        else:
            return None
    except:
        return None

HOST = 'localhost'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print('서버가 시작되었습니다.')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'클라이언트 {addr}가 연결되었습니다.')

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            if data == 'q':
                break

            result = calculate(data)
            if result is None:
                client_socket.sendall('잘못된 계산식입니다.'.encode())
            else:
                client_socket.sendall(str(result).encode())
        
        print(f'클라이언트 {addr}가 종료되었습니다.')
        client_socket.close()
