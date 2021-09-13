import socket

s = socket.socket()     #server socket
print("Socket created!!!!!!")

s.bind(('localhost',9999)) 
#take port num without string , when you get to know which is safe one

s.listen(2) #no. of connections
print("waiting for connections")

while True:
    c,address = s.accept()  #c stands for client's server
    chat = c.recv(1024).decode()
    print("Connection is with",address)
    print(chat)    

    c.send(bytes("Welcome to the server!!!!!","utf-8")) 
    # Here the utf-8 is selectes methiod type

    c.close()