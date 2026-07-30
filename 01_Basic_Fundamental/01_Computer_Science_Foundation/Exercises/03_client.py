import socket


HOST = "127.0.0.1"
PORT = 9000


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
     client.connect((HOST, PORT))

     while True:
          message = input("Enter message (type 'exit' to quit)")

          if message.lower() == "exit":
               break

          client.sendall(message.encode("utf-8"))

          response = client.recv(1024)

          print("Server:", response.decode("utf-8"))

except Exception as e:
    print("Client Error:", e)

finally:
    client.close()