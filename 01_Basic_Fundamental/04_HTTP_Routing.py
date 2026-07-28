'''
Problem Statement

Build a basic HTTP server using only Python's socket module.

The server must:

Listen on 127.0.0.1.
Use port 8080.
Accept TCP connections.
Read an HTTP request.
Parse the request method and path.
Support these routes:
GET /
GET /about
GET /health
Return:
/        → Basic HTML homepage
/about   → About message
/health  → JSON health response
Return 404 Not Found for unknown routes.
Include correct HTTP headers.
Close the client connection after sending the response.

Do not use:

Flask
FastAPI
Django
Python's http.server

Use only:

socket
Basic Python standard-library functionality

'''









import json
import socket
from typing import Tuple


HOST = "127.0.0.1"
PORT = 8080

def build_response(
        status: str,
        body: str,
        content_type: str = "text/plain; charset = utf-8"
) -> bytes:
    body_bytes= body.encode("utf-8")


    headers = [
        f"HTTP/1.1 {status}",
        f"Content-Type: {content_type}",
        f"Content-Length: {len(body_bytes)}",
        "Connection: close",
    ]

    response_head = "\r\n".join(headers) + "\r\n\r\n"

    return response_head.encode("utf-8") + body_bytes

def parse_request_line(request_text: str) -> Tuple[str, str]:
    first_line = request_text.split("\r\n", maxsplit=1)[0]

    parts = first_line.split()

    if len(parts) != 3:
        raise ValueError("Invalid HTTP request line")

    method, path, _http_version = parts

    return method, path


def handle_request(method: str, path: str) -> bytes:
    if method != "GET":
        return build_response(
            status="405 Method Not Allowed",
            body="Method Not Allowed",
        )

    if path == "/":
        return build_response(
            status="200 OK",
            body="<h1>Welcome to my HTTP server</h1>",
            content_type="text/html; charset=utf-8",
        )

    if path == "/about":
        return build_response(
            status="200 OK",
            body="<h1>About</h1><p>This server was built using sockets.</p>",
            content_type="text/html; charset=utf-8",
        )

    if path == "/health":
        body = json.dumps(
            {
                "status": "healthy",
                "server": "python-socket-server",
            }
        )

        return build_response(
            status="200 OK",
            body=body,
            content_type="application/json; charset=utf-8",
        )

    return build_response(
        status="404 Not Found",
        body="<h1>404</h1><p>Page not found.</p>",
        content_type="text/html; charset=utf-8",
    )
def run_server() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1,
    )

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)

        print(f"Server running at http://{HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()

            try:
                print(f"Connection from {client_address}")

                request_data = client_socket.recv(4096)

                if not request_data:
                    continue

                request_text = request_data.decode(
                    "utf-8",
                    errors="replace",
                )

                print(request_text)

                method, path = parse_request_line(request_text)
                response = handle_request(method, path)

            except ValueError as error:
                response = build_response(
                    status="400 Bad Request",
                    body=f"Bad Request: {error}",
                )

            except Exception:
                response = build_response(
                    status="500 Internal Server Error",
                    body="Internal Server Error",
                )

            finally:
                try:
                    client_socket.sendall(response)
                finally:
                    client_socket.close()

    except KeyboardInterrupt:
        print("\nStopping server...")

    finally:
        server_socket.close()


if __name__ == "__main__":
    run_server()