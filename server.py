import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def acceptConections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept() 
        clientName = client.recv(4096).decode().lower()
        clients[clientName] = {
            "client": client,
            "address": addr, 
            "connected_with": "",
            "file_name": "",
            "file_size": 4096
        }
        print(f"Connection established with {clientName}: {addr}")

        thread = Thread(target= handleClient, args={client, clientName})
        thread.start()

def setup():
    print("\n\t\t\t\t\t\t IP MESSENGER\n")

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print("\t\t\t\t SERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")

    acceptConections()

setup_thread = Thread(target=setup)
setup_thread.start()    