import  socket

s=socket.socket()
print("Socket created")

s.bind(('localhost', 9999))

s.listen(3)
print("waiting for connections")

while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected wih", addr)


    c.send(bytes("Welcome to Rakhi", 'utf-8'))

    c.close()

