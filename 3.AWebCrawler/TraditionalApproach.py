#!/usr/bin/env python3
#-*- coding:utf-8-*-

import socket

def fetch(url):
    sock = socket.socket()
    sock.connect(('xkcd.com',80))
    request = 'GET {} HTTP/1.0\r\nHOST:xkcd.com\r\n\r\n'.format(url)
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    #Page is now downloaded
    links = parse_links(response)
    q.add(links)