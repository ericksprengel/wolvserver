#!/usr/bin/python
#import os, sys
#from xml.etree import ElementTree as ET
import SimpleHTTPServer
import SocketServer
import importlib

PORT = 8000

def is_module(modulename):
  try:
    module = importlib.import_module(modulename)
    return True
  except ImportError:
    print("module {0} received a request, but it doesn't exist".format(modulename))
    return False

def my_api(handler, method):
  modulename = handler.path[1:].replace('/','.')
  print("path: {0}".format(modulename))
  if not is_module(modulename):
    return '{ "error_code": 404, "message": "path not found" }'


  module = importlib.import_module(modulename)
  reload(module)
  if not hasattr(module, method):
    print("module {0} received a request, but there is no method {1}".format(modulename, method))
    return '{ "error_code": 404, "message": "method not found" }'
  else:
    return getattr(module, method)(handler)


class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
    if self.path.startswith('/api'):
      self.send_response(200)
      self.send_header('Content-type','application/json')
      self.end_headers()
      self.wfile.write(my_api(self, 'get'))
      return
    else:
      #serve files, and directory listings by following self.path from
      #current working directory
      SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

  def do_POST(self):
    if self.path.startswith('/api'):
      self.send_response(200)
      self.send_header('Content-type','application/json')
      self.end_headers()
      self.wfile.write(my_api(self, 'post'))
      return
    else:
      #serve files, and directory listings by following self.path from
      #current working directory
      SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


httpd = SocketServer.ThreadingTCPServer(('', PORT),CustomHandler)

print "serving at port", PORT
httpd.serve_forever()
