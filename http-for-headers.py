#!/usr/bin/env python3

#Original Version From https://gist.github.com/phrawzty/62540f146ee5e74ea1ab

import http.server
import socketserver
import sys

PORT = int(8000 if len(sys.argv)==1 else sys.argv[1])

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('\n'+str(self.command)+' '+str(self.path))
        print(str(self.headers))
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

Handler = MyHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print("Listening on port %d..." % PORT)
httpd.serve_forever()

