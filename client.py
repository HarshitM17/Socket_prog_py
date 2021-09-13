import socket

c = socket.socket()
print("Socket created!!!!!")

c.connect(('localhost',9999))

#After running here you will get the i.p and port number(self-generated)
chat = input("Enter Message:")
c.send(bytes(chat,"utf-8"))

print(c.recv(1024).decode())#here recv is recieve and 1024 is size
