from socket import socket, AF_INET, SOCK_STREAM


HOST = 'localhost'
PORT = 4001

def get_client_socket():
    with socket(family=AF_INET, type=SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(b"Hello!")
        data = sock.recv(4096)
    print(f"Received {repr(data)}")


def send_client_message(connection, message):
    if message == "increment 5":
        return "6"

    return 'goodnight'

get_client_socket()
