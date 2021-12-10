import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

clients = []
nicknames = []

def broadcast(message, sender_client):
    for client in clients:
        if sender_client != client:
            client.send(message)
    
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            broadcast(f'{nicknames[index]} left!'.encode('ascii'), client)
            nicknames.remove(nicknames[index])
            break


while True:
    client, address = server.accept()
    print("Connected with {}".format(str(address)))

    client.send("name".encode('ascii'))
    nickname = client.recv(1024).decode('ascii')
    nicknames.append(nickname)
    clients.append(client)

    print("Nickname is {}".format(nickname))
    broadcast(f"{nickname} has joined the chat!".encode('ascii'), client)
    client.send('Connected to server!'.encode('ascii'))
    
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()