from os_speak import os_speak
def calculator():
	
	funt = input('what is the funtion you would like to do????????????\n type +,-,*,/,^\n').strip(' ')
	while not (funt == '+' or funt == '-' or funt == '/' or funt == '*' or funt == '^'):
		funt = input('you fucking idiot type a fuction\n type +,-,*,/,^\n').strip(' ') 
	
	num1 = input('what the hell is the first number???????????????\n').strip(' ' + ',')
	while num1 == '':
		num1 = input('you fucking idiot type a number\n').strip(' ' + ',')
	
	num2 = input('what the hell is the second number???????????????\n').strip(' '+',')
	while num2 == '':
		num2 = input('you fucking idiot type another number\n').strip(' ' + ',')
	
	num1= num1.strip(' ' + ',')	
	num2 = num2.strip(' ' + ',')
	if funt == '+':
		result = int(num1) + int(num2) #to add the two numbers the user inputed 
		
	if funt == '-':
		result = int(num1) - int(num2) #to subtract the two numbers the user inputed 
		
	if funt == '*':
		result = int(num1) * int(num2) #to multiply the two numbers the user inputed 
	
	if funt == '/':
		result = int(num1) / int(num2) #nice #to divide the two numbers the user inputed 
	
	if funt == '^':
		result = int(num1) ** int(num2) #to exponetuality the two numbers the user inputed 
	
	
	#this is just something i thought was funny to add in
	#it'll print the letter E a lot of times if the product is a big number
	print(result) 
	import time
	if result >= 150:
		time.sleep(3.5)	
		if result > 1000000000:
				print('R')
				time.sleep(1)
				haha = 'E' * 1000000000
				print(haha)
					
		elif result >= 10000000:
			print('R')
			hahaha = 'E' * result
			print(hahaha)
		time.sleep(1)
		os_speak("holy fuck that's big")
		time.sleep(1)
		os_speak("that's what she said")
			
		os_speak('HAHAHAHAHAHAHA')
		time.sleep(0.5)
		os_speak('HAHAHA')
		
		
	
def var():
	funt = input('what is the funtion you is in the eq???????????? \n type +,-,*,/,\n').strip(' ')
	while not (funt == '+' or funt == '-' or funt == '/' or funt == '*' or funt == '^'):
		funt = input('you fucking idiot type a fuction\n type +,-,*,/,^\n').strip(' ') 
	
	num1 = input('what the fuck is the first number you lazy peace of shit????????\n').strip(' ')
	while num1 == '':
		num1 = input('you fucking idiot type a number\n').strip(' ' + ',')
	
	eq = input('what the fuck is the product of these 2 numbers???\n').strip(' ')
	while eq == '':
		eq = input('you fucking idiot what is the number\n').strip(' ' + ',')
	
	if funt == '+': #when the fuction is addishion we need to do the opposit
		product = int(eq)-int(num1) 

	if funt == '-': #when the fuction is subtraction we need to do the opposit
		product = int(eq)+int(num1) 

	if funt == '/': #when the fuction is divishion we need to do the opposit
		product = int(eq)*int(num1) 

	if funt == '*': #when the fuction is muliplacation we need to do the opposit
		product = int(eq)/int(num1) 

	import time
	print('the varibul is\n' + str(product))
	time.sleep(2)
	os_speak('lazy bitch')
