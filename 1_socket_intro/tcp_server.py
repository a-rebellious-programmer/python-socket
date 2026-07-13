# TCP server side 
import socket


# create socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# See how to get IP address dynamically 
print(socket.gethostname()) # host-name
print(socket.gethostbyname(socket.gethostname()))


# Bind our new socket to a tuple (IP, Port)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# Put the socket into listenning mode to lissten for any possible connections
server_socket.listen()


while True:
    client_socket, client_address = server_socket.accept()
    print(type(client_socket))
    print(client_socket, '\t', client_address)
    print(type(client_address))

    print(f"You are Connected to {client_address}!\n")


    client_socket.send("You are Connected.".encode('utf-8'))

    server_socket.close()
    break
