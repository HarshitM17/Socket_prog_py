import socket
import threading

username = input("Enter your username: ")

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created!!!!!")
c.connect(('localhost',9999))

def receive():
    while True:
        try:
            message = c.recv(1024).decode('ascii')
            if message == 'name':
                c.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            c.close()
            break

def write():
    while True:
        input_msg = input('')
        message = f"{username}: {input_msg}"
        if input_msg != "": 
            c.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
