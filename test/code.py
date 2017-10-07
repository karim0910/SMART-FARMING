import socket
import os 
host = '192.168.43.50'
port = 82
address = (host, port)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)
print "Listening for client . . ."
conn, address = server_socket.accept()
while True:
   	output = conn.recv(1024);
   	print output


# os.system('bin/telegram-cli -k tg-server.pub -W -e "msg Rajkumar_ifet DRY soil"')
