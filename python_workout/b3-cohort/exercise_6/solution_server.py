from socket import socket, AF_INET, SOCK_STREAM


HOST = 'localhost'
PORT = 4001

def run_server():
    with socket(family=AF_INET, type=SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(1)
        conn, address = sock.accept()
        with conn as c:
            print(f"Connected by: {address}")
            data = c.recv(4096)
            while True:
                if not data:
                    break
                conn.sendall(data)

run_server()
