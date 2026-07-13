import socket



new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

My_host = socket.gethostname()
ip_hostname = socket.gethostbyname(My_host)

print(My_host, ip_hostname)

new_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))
print(socket.gethostbyname('digikala.com'))


new_socket.listen()
