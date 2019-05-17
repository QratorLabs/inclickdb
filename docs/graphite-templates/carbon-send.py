import socket
import time
import random


CARBON_SERVER = 'localhost'
CARBON_PORT = 2103 # write your carbon port here (default 2003)

metric_path = "servers.local.cpu.prefix.avg.middle.suffix"
value = 0 
sock = socket.socket()
sock.connect((CARBON_SERVER, CARBON_PORT))
while True:
    value = random.uniform(-100, 100) 
    time.sleep(1)
    message = '%s %s\n' % (metric_path, value)
    sock.sendall(message.encode('utf-8'))
sock.close()
