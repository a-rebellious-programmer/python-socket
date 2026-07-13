# TCP Client side 

import socket 

# create client side socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server 
host = socket.gethostbyname(socket.gethostname())
client_socket.connect((host, 12345))

message = client_socket.recv(1024)
print(message.decode('utf-8'))

# clise client side socket
client_socket.close()

