import socket
import threading


host = 'localhost'
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #server socket
print("Socket created!!!!!!")

s.bind(('localhost',9999)) 
#take port num without string , when you get to know which is safe one

s.listen(1) #no. of connections
print("waiting for connections")
usernames = []
clients= []

def broadcast(message, sender_c):
    for c in clients:
        if sender_c != c:
            c.send(message)
    
def handle(c):
    while True:
        try:
            message = c.recv(1024)
            broadcast(message, c)
        except:
            index = clients.index(c)
            clients.remove(c)
            c.close()
            broadcast(f'{username[index]} left!'.encode('ascii'), c)
            username.remove(username[index])
            break


while True:
    c,address = s.accept()  #c stands for client's server
    print("Connected with {}".format(str(address)))
    
    c.send("name".encode('ascii'))
    username = c.recv(1024).decode('ascii')
    usernames.append(username)
    clients.append(c)

    # chat = c.recv(1024).decode()


    print("Username is {}".format(username))
    broadcast(f"{username} has joined the chat!".encode('ascii'), c)
    c.send('Connected to server!'.encode('ascii'))

    c.send(bytes("Welcome to the server!!!!!","utf-8")) 
    # Here the utf-8 is selectes methiod type

    thread = threading.Thread(target=handle, args=(c,))
    thread.start()