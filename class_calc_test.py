import time
class calcculator:
	
	
	def  cal():
		#try to use eval() with local scope
		
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
		print(result)
		time.sleep(2)
		print('do it yourself next time bitch')
		
		
		
	def var():
		funt = input('what is the fucking funtion in your eq???????????? \n type +,-,*,/,\n').strip(' ')
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

		
		print('the varibul is\n' + str(product))
		time.sleep(2)
		#os_speak('lazy bitch')

