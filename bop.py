from subprocess import *
from calculator import calculator
from os_speak import os_speak,ohno
import time
from datetime import datetime
from find_var import var
import playsound

path = '/home/kevin/Documents/bop/dep/'


#these is so when we use the os_speak we can hear what it says 
call(["amixer", "-D", "pulse", "sset", "Master", "70%","on"]) #this is used to run a command to set the master volume to 70%
call(['clear'])

#prerequisites 
first_name= input('what is your first name!!!!!!?????\n').capitalize().strip(' ')
last_name= input('what is your last name!!!!!!!!??????\n').capitalize().strip(' ')
output = f'Hello, {(first_name)} {(last_name)}'
output_c= f'{(first_name)} {(last_name)}'

index1 = 6
def count_down(num):
	if num == 'true':
		playsound.playsound(path + 'audio-' + str(index1) + '.mp3')
	elif num == 'false':
		playsound.playsound(path + 'audio-' + 'SELF-DESTRUCT_SEQUENCE_INITIATED' + '.mp3')

if first_name =='Kevin' and last_name =='Hill' or first_name== 'Dani' and last_name == 'Hill' or first_name=='Melani' :
		allow_acsess= True #this is a boolion variabule used in the code later 
else:
	 print(output_c + ' is not autorized to use this program')
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
			 #call(['shutdown','-h','now']) #this uses the call fuction to tell the computer to shutdown
if allow_acsess:
	print(output_c + ' is autorized to use this program')
	print(output)
	time.sleep(3)
	print('How was your day ' + output_c + '?')
	h_day = input("Please type 1 for 'good' or, 2 for 'bad'.\n")
	if h_day == '1':
		print("I'm happy to hear that.")
		time.sleep(3)
		#input1 = input('How may I help?')
	if h_day == '2':
		print("Oh no! I'm sorry to here that.")
		time.sleep(3)
		#input2 = input('How can I make it better?')
	print("I'm a new programe so I can't do to much but I can do simpal math, \n but I don't like it so I may be a litte agressive")
	print('\n')
	time.sleep(2)
	options = ['calculator', 'find var']
	print(str(options) + ' are all I can do at the moment' ) 
	want= input('For ' + str(options[:1]) +' type "cal" or for ' + str(options[1:3]) + 'just type var\n').strip(' ')
	#a simpale calculator 
	if want == 'cal':
		calculator()
	#This is to find the varibule in almost any eqaison
	if want == 'var':
		var()
	
