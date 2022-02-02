import socket

# create a INET, STREAMING socket.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to public host, and port 1234.
serversocket.bind((socket.gethostname(), 1234))

# queue up as many as 5 connection requests before refusing outside connections.
serversocket.listen(5)

while True:
    # accept connections from outside.
    (clientsocket, address) = serversocket.accept()
    print(f"Connection from {address} has been established!")
    welcome_msg = "Welcome to the server!"
    clientsocket.send(welcome_msg.encode())