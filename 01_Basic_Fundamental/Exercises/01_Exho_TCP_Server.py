'''
Problem statement

Build a TCP server that:

Listens on port 9000
Accepts a client
Receives a message
Sends the same message back

Example:

Client sends: hello
Server sends: hello

Purpose:

Understand sockets
Understand bind, listen, accept, receive, and send
'''

import socket

HOST = "127.0.0.1"
PORT = 9000

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to IP and port
server_socket.bind((HOST, PORT))

# Listen for one incoming connection
server_socket.listen(1)

print(f"Server is running at http://{HOST}:{PORT}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Client:", client_address)

# Receive data from the client
request_data = client_socket.recv(1024)

# Display the received message
print("Received:", request_data.decode("utf-8"))

# Send the same data back (echo)
client_socket.sendall(request_data)
# Close the client connection
client_socket.close()

# Close the server socket
server_socket.close()

