
#Version0.1
#Author: WhaleChen(whalechen123@gmail.com)

#-*- coding:utf-8 -*-
from os.path import exists

# type the name of a diary book, ENTER for 'diarybook'
print "Please enter the diary name: "
diaryName = raw_input("> (ENTER for 'diarybook')")

if diaryName == "":
	diaryName = "diarybook"

fileName = diaryName +".txt"

# check if the name exists
# if not, create a new txt file using the name typed
# use the method from suluren
print "Please write diary: "	
if exists(fileName) == True:
	diary = open(fileName,'a+')
	diaryAlreadyWritten = diary.read()
	print diaryAlreadyWritten

else:
	diary = open(fileName,'w')

# Before write diary,first put the current position to the end
diary.seek(0,2)

# write diary
# use the method from suluren 
line ="test"
while len(line) != 0:
	line = raw_input(">(ENTER for quit)")
	diary.write("\n"+ line)	
	
# close diary book 
diary.close()

	
#time should be added in 
#use class may be more readable
#def writefile(openedFile) may be ok? 
#GetOriginData from other files
#test Chinese 

	
	

	






	
	
	
	
