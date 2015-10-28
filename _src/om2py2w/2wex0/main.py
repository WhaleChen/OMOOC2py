#-*- coding:utf-8 -*-
import Tkinter
from Tkinter import *
from os.path import exists

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("Pls enter the text here")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)
		
    
    def print_contents(self, event):
        
		print "You write >>>", \
              self.contents.get()
		diary.write("\n"+self.contents.get())
		# the process is the same as the first work. 
		
	
def write_files():
	filename = "diary.log"
	if exists(filename) == True:
	    diary =open(filename,'a+')
		
	    diaryAlreadyWitten =diary.read()
	    print diaryAlreadyWitten
	else:
		diary =open(filename,'w')
	diary.seek(0,2)
	  

root = Tk()
root.geometry('200x200')
#To adjust the window size
app = App(master =root)
filename = "diary.log"
if exists(filename) == True:
	diary =open(filename,'a+')
		
	diaryAlreadyWitten =diary.read()
	print diaryAlreadyWitten
else:
	diary =open(filename,'w')
diary.seek(0,2)
#write_files()
#I do not know how to make module with the name write_files()
app.mainloop()

root = destroy()
