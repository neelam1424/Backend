'''
Problem statement

Build a server that receives text and returns it in uppercase.

Input: hello server
Output: HELLO SERVER

Add:

Empty-input handling
UTF-8 decoding
Exception handling
'''



import socket

HOST = "127.0.0.1"
PORT= 9000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))

server_socket.listen(1)

try:
    client_socket, client_address = server_socket.accept()
    print(f"Client: {client_address}")

    while True:
        request_data = client_socket.recv(1024)

        # Client disconnected
        if not request_data:
            print("Client disconnected")
            break

        try:
            # Decode UTF-8
            message = request_data.decode("utf-8")


            # Empty input handling

            if message.strip() == "":
                response = "Error: Empty input received."

            else:
                response = message.upper()


            #send response

            client_socket.sendall(response.encode("utf-8"))

        except UnicodeDecodeError:
            error = "Error: Invalid UTF-8 data."
            client_socket.sendall(error.encode("utf-8"))

except Exception as e:
    print("Server Error:", e)

finally:
    client_socket.close()
    server_socket.close()
    print("Server closed.")

