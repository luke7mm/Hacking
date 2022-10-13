#Copied from https://www.geeksforgeeks.org/python-network-programming/
#Not my own work

import socket

s = socket.socket()
print("Socket successfully created")

port = 40674

s.bind('', port))
print("socket binded to %s" %(port))

s.listen(5)
print("Socket is listening")

while True:

    c, addr = s.accept()
    print('Got the connection from', addr)

    c.send(b'Thank you for connecting')

    c.close()
