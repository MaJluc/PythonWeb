import socket
from concurrent.futures import ThreadPoolExecutor

TCP_IP = 'localhost'
TCP_PORT = 8080
CHUNK_BYTES = 1024
ID = 0


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(5)
        print(f'Start server {s.getsockname()}')
        with ThreadPoolExecutor(5) as client_pool:
            while True:
                try:
                    new_sock, address = s.accept()
                    client_pool.submit(handle, new_sock, address, get_id())
                except KeyboardInterrupt:
                    print(f'Server close')


def handle(conn: socket.socket, address: str, id_user: int):
    print(f'Connection User_{id_user} from {address}')
    with conn:
        while True:
            data = conn.recv(CHUNK_BYTES).decode()
            if not data:
                print(f'User_{id_user} stopped app')
                break
            print(f'received message from User_{id_user}: {data}')
            message = input(f'Answer to {id_user} --> ')
            conn.send(message.encode())


def get_id():
    global ID
    ID += 1
    return ID


if __name__ == '__main__':
    main()
