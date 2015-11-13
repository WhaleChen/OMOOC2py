#-*- coding:utf-8 -*-
#the 4th week bottle exercise

##############################################
#file#######################################
######################################
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

################################################
#bottle###################################
#############################################
from bottle import Bottle,run,template,request,debug
import socket
app =Bottle()
@app.route('/')
def mainpage():
    mydiary = initiate_files()
    welcome ='''
<p>Python's Advanture:</p>
'''
    form_area ='''
<form action="/" method ="get">
diary: <input name="diary" type="text" id="diary" >
diaryOutput: <input name="dairy" type="text" id="output">
<br/>
<button onclick="document.getElementById('output').value=document.getElementById('diary').value">All Done</button>
<br/>
This is a try
<input type="submit" value="Read txt" />
</form>
'''
    
    return welcome +form_area + template('write',diaryWritten='Hello')
@app.route('/write')
def write():
    global mydiary
    mydiary = initiate_files() # define mydiary can be used anywhere
    return template('write',diaryWritten=diaryAlreadyWritten)
@app.route('/write/<name>',method='POST')
def do_write(name ='Whale'):
    diaryInput =request.forms.get('diaryInput')
    mydiary.write(diaryInput)
    mydiary.seek(0,0)
    diaryAlreadyWritten =mydiary.read()
    #quitProgram =request.forms.get('quit')
    #print quitProgram
    #return app.template('write',diaryWritten=diaryAlreadyWritten)
debug(True)
run(app, host='localhost', port =8080,reloader=True)
