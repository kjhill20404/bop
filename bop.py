from subprocess import call
call(["amixer", "-D", "pulse", "sset", "Master", "60%"])

first_name= input('what is your first name!!!!!!?????\n').lower().strip(' ')
last_name= input('what is your last name!!!!!!!!??????\n').lower().strip(' ')
output = f'Hello, {(first_name.capitalize())} {(last_name.capitalize())}'
output_c= f'{(first_name.capitalize())} {(last_name.capitalize())}'

from os_speak import os_speak
import time

if first_name =='kevin' and last_name =='hill' or first_name== 'dani' or first_name=='melani' :
		allow_acsess= True #this is a boolion variabule used in the code later 
else:
	 print(output_c + ' is not autorized to use this program')
	 os_speak('SELF-DESTRUCT SEQUENCE INITIATED')
	 from datetime import datetime
	 print(datetime.now())
	 allow_acsess= False	 
		
	 index1 = 6
	 while index1 > 0: #this counts down 
		 print(' in '+ str(index1) +' seconds')
		 os_speak(str(index1))
		 time.sleep(1)
		 index1 = index1 - 1
		 while index1 == 1: # when index1 is equle to 1 it waits one sec and say's boom
			 print(' in 1 second')
			 os_speak('1')
			 time.sleep(1)
			 print(' BOOM')
			 index1 = index1 -1 
if allow_acsess:
	print(output_c + ' is autorized to use this program')
	print(output)
	time.sleep(3)
	print('How was your day ' + output_c + '?')
	h_day = input("Please type 1 for 'good' or, 2 for 'bad'. ")
	if h_day == '1':
		print("I'm happy to hear that.")
		time.sleep(3)
		input1 = input('How may I help?')
	if h_day == '2':
		print("Oh no! I'm sorry to here that.")
		time.sleep(3)
		input2 = input('How can I make it better?')


	print("I'm a new programe so I can't do to much but I can do simpal math, \n but I don't like it so I may be a litte agressive")
	print('\n')
	time.sleep(2)
	options = ['calculator', 'find var']
	print(str(options) + ' are all i can do at the moment' ) 
	want= input('For ' + str(options[:1]) +' type "cal" or for ' + str(options[1:3]) + 'just type var\n').strip(' ')
	
	if want == 'calculator':
		from calculator import calculator
		calculator()
	#This is to find the varibule in almost any eqaison
	if want == 'var':
		from find_var import var
		var()
