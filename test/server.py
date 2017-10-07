# echo_server.py
import socket
import os

host = '192.168.43.50'        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    print data
    if data=='on':
       	os.system('../tg/bin/telegram-cli -k tg-server.pub -W -e "msg Rajkumar_ifet DRY soil"')
    else:
    	os.system('../tg/bin/telegram-cli -k tg-server.pub -W -e "msg Rajkumar_ifet Motor Off"')
       	
conn.close()