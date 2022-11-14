import socket


TCP_IP = 'localhost'
TCP_PORT = 8080
CHUNK_BYTES = 1024


def client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((TCP_IP, TCP_PORT))
            print(f'Run')

            while True:
                message = input('--> ')
                if message.lower().strip() == 'stop':
                    print('Stopped')
                    break
                s.send(message.encode())
                data = s.recv(CHUNK_BYTES).decode()
                print(f'Received message: {data}')
    except (ConnectionResetError, BrokenPipeError, ConnectionRefusedError) as e:
        print(f'Connection not established. {e}')


if __name__ == '__main__':
    client()
