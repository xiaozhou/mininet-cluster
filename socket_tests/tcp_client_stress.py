#!/usr/bin/env python

import socket
import sys
from datetime import datetime

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

remote_ip = '10.211.55.12'
#remote_ip = '10.0.0.1'
port = 5000

s.connect((remote_ip , port))

datalen = 0
num = 0
message = ''
msglen = 1000
if len(sys.argv) > 1:
    msglen = int(sys.argv[1])
for i in range(msglen):
    message += '#'
time = datetime.now()
while(1):
    try:
        s.sendall(message)
        datalen += msglen
        num += 1
        if num % 100000 == 0:
            delta = datetime.now() - time
            diff = delta.seconds + delta.microseconds/1E6
            speed = datalen/1E6/diff * 8
            print 'bytes: %d, time %.2f sec, speed %.2f Mbps' % (datalen, diff, speed)
            time = datetime.now()
            datalen = 0
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
