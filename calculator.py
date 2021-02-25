funt =input('what is the funtion you would like to do????????????\n type +,-,*,/,^\n')
num1 =input('what the hell is the first number???????????????\n').strip(' ')
num2 = input('what the hell is the second number???????????????\n').strip(' ')


if funt == '+':
	result = int(num1) + int(num2) #to add the two numbers the user inputed 

elif funt == '-':
	result = int(num1) - int(num2) #to subtract the two numbers the user inputed 

elif funt == '*':
	result = int(num1) * int(num2) #to multiply the two numbers the user inputed 

elif funt == '/':
	result = int(num1) / int(num2) #to divide the two numbers the user inputed 

elif funt == '^':
	result = int(num1) ** int(num2) #to exponetuality the two numbers the user inputed 



print(result) 
import time
if result >= 150:
	time.sleep(3.5)	
	if result >= 10000000:
		print('R')
		if result > 1000000000:
			haha = 'E' * 1000000000
			print(haha)
	else:
		hahaha = 'E' * result
		print(hahaha)
	time.sleep(1)
	print("holy fuck that's big")
	time.sleep(1)
	print("that's what she said")

