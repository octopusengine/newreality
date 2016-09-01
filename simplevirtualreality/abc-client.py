#!bin/usr/env python
#https://www.reddit.com/r/learnpython/comments/3ffiy6/trying_to_make_a_fullduplex_chat_system/

import socket
from time import ctime
import threading

print("---client---")

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = 'localhost'
##host = '192.168.0.45' ##server.ok
port = 1212 #12345                # Reserve a port for your service.
print("host: "+host + " /"+str(port))

sADDR = (host, port)
buff = 1024

cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSock.connect(sADDR)

def receive():
    while True:
        rMessage = cliSock.recv(buff)
        if not rMessage:
            print "Ending connection"
            break
        print "[{0}]: {1}".format(ctime(), rMessage)

def send():
    while True:
        sMessage = raw_input(">>")
        cliSock.send(sMessage)

t1snd = threading.Thread(target=send, name=1)
t2rec = threading.Thread(target=receive, name=2)

t1snd.start()
t2rec.start()
