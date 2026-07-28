import socket

HOST = "127.0.0.1"
PORT = 8080

# How will you create a TCP socket?
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)


# How will you bind it to an IP address and port?
server_socket.bind((HOST, PORT))

# How will the server wait for clients?
server_socket.listen()

print(f"Server is running at http://{HOST}:{PORT}")

while True:
    client_socket , client_address = server_socket.accept()

    request_data = client_socket.recv(1024)
    print("Client:", client_address)

    print(request_data.decode("utf-8"))


    response_body = "<h1>Hello from my Python server</h1>"

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{response_body}"
    )

    client_socket.sendall(response.encode("utf-8"))
    client_socket.close()