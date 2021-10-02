#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = 192.168.43.64
host = socket.gethostname()
port = 555

serversocket.bind((host, port))

serversocket.listen(3)

while True:
     clientsocket, address = serversocket.accept()

     print("received connection from" %str(address))
     
     message = "Hello, Thankyou for connecting to the server" + "\r\n"
     clientsocket.send(message.encode('ascii'))

     clientsocket.close() 