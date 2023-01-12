from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import ssl
import sys

if len(sys.argv)<4:
  print("Usage https.py listenIP port path/to/key.pem path/to/cert.pem")

listenip = sys.argv[1]
port = int(sys.argv[2])
keyfile = sys.argv[3]
certfile = sys.argv[4]

httpd = HTTPServer((listenip,port), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=keyfile, certfile=certfile, server_side=True)
httpd.serve_forever()
print("Serving on "+port)

# gen self-signed key with: 
#   openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
#   pem password: "pass"
