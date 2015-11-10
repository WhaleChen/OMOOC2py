# -*- coding: utf-8 -*-
"""
This is the first server file 
"""

########################################################################
#initiate_files ############################################################### 
########################################################################
from os.path import exists	    
def initiate_files():
        global diaryAlreadyWritten
	filename ="diary.log"
	if exists(filename)==True:
		diary =open(filename,'a+')
		diaryAlreadyWritten=diary.read()
		print diaryAlreadyWritten
	else:
		diary =open(filename,'w')
		diaryAlreadyWritten="Welcome and Enjoy your Diary!\n"
		diary.write(diaryAlreadyWritten)
		
	diary.seek(0,2)
	return diary

########################################################################
# Server ############################################################### 
########################################################################

import socket
import sys

#def server(host,port)
host ="localhost"  
port =10000
sock =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host,port)
sock.bind(server_address)
diary = initiate_files()
dataBase =[]
while True:
	while dataBase ==[]:
	    line =raw_input(">>>")
	    diary.write(line +'\n')
	    if line =="":
		    break
	#print "\nwaiting to receive data."
	data,address =sock.recvfrom(4096)
	#print "received %s bytes data from %s"%(len(data),address)
	dataBase.append(data)
	print type(data)
	print len(data)
	print len(dataBase)
	if len(dataBase)==1:
		sent=sock.sendto(diaryAlreadyWritten,address)
	elif len(dataBase)>1 and len(data)>=1:
		diary.write(data+'\n')
		print data
	elif len(dataBase)>1 and len(data)==0:
		diary.close()
		diary = initiate_files()
		dataBase =[]
		data =None
		address =None
		
		
	else:
		print "I do not know"


