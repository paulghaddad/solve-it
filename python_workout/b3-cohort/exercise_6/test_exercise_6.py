import pytest
import socket
from threading import Thread

from solution_server import run_server
from solution_client import get_client_socket, send_client_message


@pytest.fixture
def running_server():
    print("Running server")
    t = Thread(target=run_server, daemon=True)
    t.start()
    yield
    print("Tearing down server")


def test_say(running_server):
    print("In test_say, about to get client socket")
    client_socket = get_client_socket()
    print("In test_say, about to send message")
    assert send_client_message(client_socket, 'say goodnight') == 'goodnight'


def test_increment(running_server):
    client_socket = get_client_socket()
    assert send_client_message(client_socket, 'increment 5') == '6'
