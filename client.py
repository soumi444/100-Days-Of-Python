import socket

c=socket.socket()
c.connect(('localhost', 9999))

name = input("Enter your name:")
c.send(bytes(name,'utf-8').decode())

print(c.recv(1024).decode())
