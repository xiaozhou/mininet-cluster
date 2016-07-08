#!/usr/bin/env python

import socket
import sys
 
HOST = ''   
PORT = 5000 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'

conn, addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])

opt = 0

if len(sys.argv) > 1:
    opt = int(sys.argv[1])

while 1:     
    data = conn.recv(8192)
    if not data: 
        break     

    if opt == 0:
        datalen = len(data)
        reply = 'recv data with ' + str(len(data)) + ' bytes'
        conn.sendall(reply)
        print reply
    elif opt == 1:
        reply = 'OK...' + data
        conn.sendall(reply)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
 
conn.close()
s.close()
