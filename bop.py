from os_speak import os_speak
from subprocess import *
from calculator import calculator,var
from os_speak import os_speak,ohno
import time
from datetime import datetime
import playsound


path_to_file = '/home/kevin/Documents/bop/dep/'
#these is so when we use the os_speak we can hear what it says 
#call(["amixer", "-D", "pulse", "sset", "Master", "70%","on"]) #this is used to run a command to set the master volume to 70%
call(['clear'])

#prerequisites 
first_name= input('what is your first name!!!!!!?????\n').capitalize().strip(' ')
last_name= input('what is your last name!!!!!!!!??????\n').capitalize().strip(' ')
output = f'Hello, {(first_name)} {(last_name)}'
output_c= f'{(first_name)} {(last_name)}'

attemps = 1

index1 = 6
def count_down(num):
	if num == 'true':
		playsound.playsound(path_to_file + 'audio-' + str(index1) + '.mp3')
	elif num == 'false':
		playsound.playsound(path_to_file + 'audio-' + 'SELF-DESTRUCT_SEQUENCE_INITIATED' + '.mp3')

def allow_acsess():
	self_destruct = False
	print(output_c + ' is autorized to use this program')
	print(output)
	time.sleep(3)
	print('How was your day ' + output_c + '?')
	h_day = input("Please type 1 for 'good' or, 2 for 'bad'.\n")
	if h_day == '1':
		print("I'm happy to hear that.")
		time.sleep(3)
	if h_day == '2':
		print("Oh no! I'm sorry to here that.")
		time.sleep(3)
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


if first_name =='Kevin' and last_name =='Hill' or first_name== 'Dani' and last_name == 'Hill' or first_name=='Melani' :
	aa = True #for the allow_acsess class 
	allow_acsess() #this is a boolion variabule used in the code later 
	self_destruct = False
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
				allow_acsess()
			if attempts == 4:
				aa = True
	while attemps == 4:
		self_destruct = True
		aa = True
		attemps = attemps + 1
	while attemps == 5:
		self_destruct = False 

if self_destruct == True: #play a sound and shuts down the device
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
			call(['shutdown','-h','now']) #this uses the call fuction to tell the computer to shutdown, you can comment it out if you want 


