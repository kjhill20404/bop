from os_speak import os_speak
from subprocess import *
from calculator import calculator,var
from os_speak import os_speak,ohno
import time
from datetime import datetime
import playsound


path_to_file = '/home/kevin/bop/dep/'
#these is so when we use the os_speak we can hear what it says 
#call(["amixer", "-D", "pulse", "sset", "Master", "70%","on"]) #this is used to run a command to set the master volume to 70%
call(['clear'])

#prerequisites 
first_name= input('what is your first name!!!!!!?????\n').capitalize().strip(' ')
last_name= input('what is your last name!!!!!!!!??????\n').capitalize().strip(' ')
output_c= (first_name) + ' '+ (last_name)
#var to be used later
attemps = 1

index1 = 6
#classes used later
def count_down(num):#this is used in self_destruct just so the code is a little more readbule
	if num == 'true':
		playsound.playsound(path_to_file + 'audio-' + str(index1) + '.mp3')
	else:
		playsound.playsound(path_to_file + 'audio-' + 'SELF-DESTRUCT_SEQUENCE_INITIATED' + '.mp3')



#this is the main function that gets used and to be added onto going forword
def allow_acsess():
	self_destruct = False
	print(output_c + ' is authorized to use this program')
	print('Hello, ' + output_c)
	os_speak(output_c + ' is authorized to use this program')
	os_speak('Hello, ' + output_c)
	time.sleep(3)
	print("I'm a new programe so I can't do to much but I can do simpal math, \n but I don't like it so I may be a little agressive")
	print('\n')
	os_speak("I'm a new programe so I can't do to much but I can do simpal math, but I don't like it so I may be a little agressive")
	time.sleep(2)
	options = ['calculator', 'find variable']
	print(str(options) + ' are all I can do at the moment' ) 
	os_speak(str(options) + ' are all I can do at the moment' )
	want= input('For ' + str(options[:1]) +' type "cal" or for ' + str(options[1:3]) + 'just type var\n').strip(' ')
	#a simpale calculator 
	if want == 'cal':
		calculator()
	#This is to find the varibule in almost any eqaison
	elif want == 'var':
		var()
	else:
		want = input("I'm sorry, I don't understand. Is their something less complex I may help with?")

#this checks to see if the name people enter is allowed (change names if nessissary)
if first_name =='Kevin' and last_name =='Hill' or first_name== 'Dani' and last_name == 'Hill' or first_name=='Melani' :#could theoredicly put names in list going forward
	aa = True #for the allow_acsess class
	self_destruct = False
	allow_acsess() #this is a boolion variabule used in the code later
else:
	aa = False
	while attemps < 4:
		while aa == False:#to give the user a couple extra attempts if they made a mistake
			first_name = input("let's try that again shall we, what is your first name??").capitalize().strip(' ')
			last_name = input('and your last name??').capitalize().strip(' ')
			attemps = attemps + 1
			if first_name =='Kevin' and last_name =='Hill' or first_name== 'Dani' and last_name == 'Hill' or first_name=='Melani' :
				aa = True
				attemps = 5
				self_destruct = False
				output_c= f'{(first_name)} {(last_name)}'
				allow_acsess()
			elif attemps == 4:
				self_destruct = True
				aa = False
				output_c= f'{(first_name)} {(last_name)}'
				attemps = attemps + 70
		while attemps == 5:
			self_destruct = False 

#this is to maybe scare the unauthorized user index1 was prev deffinded in the begining of the code
if self_destruct == True: #play a sound and shuts down the device
	print(output_c + ' is not authorized to use this program')
	os_speak(output_c + ' is not authorized to use this program')
	print('SELF-DESTRUCT SEQUENCE INITIATED')
	count_down('false')
	print(datetime.now())
	allow_acsess= False
	while index1 > 0: #this counts down 
		print('in '+ str(index1) +' seconds')
		count_down('true')
		time.sleep(1)
		index1 = index1 - 1
		while index1 == 1: # when index1 is equle to 1 it waits one sec and say's boom
			print('in 1 second')
			count_down('true')
			time.sleep(1)
			ohno()#this will play a exploshion sound as long as its in the same folder
			time.sleep(1)
			index1 = index1 -1 
#			call(['shutdown','-h','now']) #this uses the call fuction to tell the computer to shutdown, you can comment it out if you want 


