from os_speak import os_speak
def var():
	func = input('what is the funtion you is in the eq???????????? \n type +,-,*,/,\n').strip(' ')
	first_num = input('what the fuck is the first number you lazy peace of shit????????\n').strip(' ')
	eq = input('what the fuck is the product of these 2 numbers???\n').strip(' ')

	if func == '+': #when the fuction is addishion we need to do the opposit
		product = int(eq)-int(first_num) 

	if func == '-': #when the fuction is subtraction we need to do the opposit
		product = int(eq)+int(first_num) 

	if func == '/': #when the fuction is divishion we need to do the opposit
		product = int(eq)*int(first_num) 

	if func == '*': #when the fuction is muliplacation we need to do the opposit
		product = int(eq)/int(first_num) 

	import time
	print(product)
	time.sleep(2)
	os_speak('lazy bitch')
