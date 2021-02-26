first_name= input('what is your first name!!!!!!?????\n').lower().strip(' ')
last_name= input('what is your last name!!!!!!!!??????\n').lower().strip(' ')
output = f'Hello, {(first_name.capitalize())} {(last_name.capitalize())}'
output_c= f'{(first_name.capitalize())} {(last_name.capitalize())}'

import time

if first_name =='kevin' and last_name =='hill' or first_name== 'dani' or first_name=='melani' :
        allow_acsess= True #this is a boolion variabule used in the code later 
else:
     print(output_c + ' is not autorized to use this program')
     print('SELF-DESTRUCT SEQUENCE INITIATED')
     from datetime import datetime
     print(datetime.now())
     allow_acsess= False     
        
     index1 = 6
     while index1 > 0: #this counts down 
         print(' in '+ str(index1) +' seconds')
         time.sleep(1)
         index1 = index1 - 1
         while index1 == 1: # when index1 is equle to 1 it waits one sec and say's boom
             print(' in 1 second')
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

print("I'm a new programe so i can't do to much but i can do simpal math, \n but i don't like it so i may be a litte agressive")
print('\n')
time.sleep(2)

funt = input('what is the funtion you would like to do????????????\n type +,-,*,/,^\n')
num1 = input('what the hell is the first number???????????????\n').strip(' ' + ',')
num2 = input('what the hell is the second number???????????????\n').strip(' '+',')

num1= num1.strip(' ' + ',')
num2 = num2.strip(' ' + ',')
if funt == '+':
	result = int(num1) + int(num2) #to add the two numbers the user inputed 

if funt == '-':
	result = int(num1) - int(num2) #to subtract the two numbers the user inputed 

if funt == '*':
	result = int(num1) * int(num2) #to multiply the two numbers the user inputed 

if funt == '/':
	result = int(num1) / int(num2) #to divide the two numbers the user inputed 

if funt == '^':
	result = int(num1) ** int(num2) #to exponetuality the two numbers the user inputed 



print(result) #nice 
import time
if result >= 150:
	time.sleep(3.5)	
	if result > 1000000000:
			print('R')			
			time.sleep(1)
			haha = 'E' * 1000000000
			print(haha)
			brake
	elif result >= 10000000:
		print('R')
		hahaha = 'E' * result
		print(hahaha)
	time.sleep(1)
	print("holy fuck that's big")
	time.sleep(1)
	print("that's what she said")

