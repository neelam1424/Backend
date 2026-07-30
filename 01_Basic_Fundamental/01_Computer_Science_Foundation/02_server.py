from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
server.serve_forever()