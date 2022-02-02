import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket.connect((socket.gethostname(), 1234))

# recieve data from server.
data_from_server = clientsocket.recv(1024)

print(data_from_server.decode())