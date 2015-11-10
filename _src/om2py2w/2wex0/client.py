#-*- coding:utf-8 -*-
"""
This is the first client file
"""
####################################################
#client##############################################
##################################################

import socket
import sys
server_address =('localhost',10000)
sock =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto('hello',server_address)
server_data,server_addr = sock.recvfrom(4096)
print server_data
if server_data:
	print "What you want to write:"
	while True:   
	    line =raw_input(">>>")
	    # the data written send to server at once
	    sock.sendto(line,server_addr)
	    if len(line) ==0:
		    break


