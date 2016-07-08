#!/usr/bin/env python

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

#remote_ip = '10.211.55.12'
remote_ip = '10.0.0.2'
port = 5000

s.connect((remote_ip , port))

opt = 0

if len(sys.argv) > 1:
    opt = int(sys.argv[1])

while(1):
    if opt == 0:
        message = ''
        msglen = int(raw_input('Enter message length: '))
        for i in range(msglen):
            message += '#'
    else:
        message = raw_input('Enter message to send : ')
    try:
        s.sendall(message)
        reply = s.recv(4096)
        print 'Server reply: ' + reply
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
