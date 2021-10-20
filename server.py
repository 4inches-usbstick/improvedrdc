import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
import cgi

import cgitb
cgitb.enable()

import os

def fileio(name, mode, contents = ""):
    f = open(name, mode)
    if mode == 'r':
        tr = f.read()
    if mode == 'rb':
        tr = f.read()
    if mode == 'a' or mode == 'w':
        f.write(contents)
        tr = None
    if mode == 'ab' or mode == 'wb':
        f.write(contents)
        tr = None
    f.close()
    return tr
    
def interface_exec(file):
    handle = __import__(file)
    return handle.doGET()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Methods','GET')
        self.send_header('Access-Control-Allow-Headers','Origin, Content-Type, X-Auth-Token, Cache-Control')
        self.end_headers()
        url = unquote(self.path).split('?')
        if len(url) == 1: url.append('')

        if url[0][-4:] == '.dpy':
            params0 = url[1].split('&')
            finalparams = {}
            for i in params0:
                i2 = i.split('=')
                finalparams[i2[0]] = i2[1]
                msg = __import__(url[0].split('/')[-1].replace('.dpy','')).doGET(finalparams)
        elif url[0][-5:] == '.html':
            try: msg = fileio(url[0].split('/')[-1], 'r')
            except: msg = fileio('404.html', 'r')
        else:
            msg = '<h1>403 Forbidden</h1><hr>File direct access is forbidden.'

        self.wfile.write(bytes(str(msg), 'utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Methods','GET')
        self.send_header('Access-Control-Allow-Headers','Origin, Content-Type, X-Auth-Token, Cache-Control')
        self.end_headers()
        url = self.path
        print(url)
    
        if url[-4:] == '.dpy':
            finalparams = {}
            content_len = int(self.headers.get('Content-Length'))
            post_body = str(self.rfile.read(content_len))[:-1].replace("b'","")
            fparams = post_body.split('&')
            for i in fparams:
                i2 = i.split('=')
                finalparams[i2[0]] = i2[1]
            msg = __import__(url.split('/')[-1].replace('.dpy','')).doPOST(finalparams)
        
      
            

        else:
            msg = '<h1>403 Forbidden</h1><hr>HTTP POST not allowed for non DPY files.'

        self.wfile.write(bytes(str(msg), 'utf-8'))
       



with HTTPServer(('', int(fileio('port.txt','r'))), handler) as server:
    print('Server started.')
    server.serve_forever()
