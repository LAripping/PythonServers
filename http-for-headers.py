#!/usr/bin/env python

#Original Version From https://gist.github.com/phrawzty/62540f146ee5e74ea1ab

import SimpleHTTPServer
import SocketServer
import logging
import sys

PORT = (8000 if len(sys.argv)==1 else sys.argv[-1])

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.error('\n'+str(self.headers))
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Listening on port %d..." % PORT
httpd.serve_forever()

