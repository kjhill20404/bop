
from subprocess import *
from calculator import calculator,var
import time
from datetime import datetime
import playsound
from gtts import gTTS
import os 
import random 
import platform 

if(platform.system() == 'Windows'):
	call(["cls"],shell=True)
elif(platform.system() == 'Linux'):
	call(["clear"],shell=True)
	call(["amixer", "-D", "pulse", "sset", "Master", "70%","on"],shell = True) #this is used to run a command to set the master volume to 70%


path_to_file = '/home/kevin/bop/dep/'
#these is so when we use the os_speak.string we can hear what it says 



#prerequisites 
first_name= input('what is your first name!!!!!!?????\n').capitalize().strip(' ')
last_name= input('what is your last name!!!!!!!!??????\n').capitalize().strip(' ')
output_c= (first_name) + ' '+ (last_name)
#var to be used later
attemps = 1

index1 = 6
#classes used later
class os_speak:
	def __init__(self):
		self.audio_string = str()

	def string(astring):
		audio_string = astring
		# tts = gTTS(text=audio_string, lang='en') 
		# r = random.randint(1, 1000000)
		# audio_file = 'audio-' + str(r) + '.mp3'
		# tts.save(audio_file)
		print(audio_string +"\n")
		# playsound.playsound(audio_file)
		# os.remove(audio_file)
	def path(file):
		print('assume the file was played')
		# playsound.playsound(file)
	def ohno():
		print('ohno')
		# path = '/home/kevin/bop/dep/'
		# playsound.playsound(path + 'battle003.mp3')
	def count_down(bool,num):#this is used in self_destruct just so the code is a little more readbule
		print('')
		# if bool == True:
		# 	playsound.playsound(path_to_file + 'audio-' + str(num) + '.mp3')
		# else:
		# 	playsound.playsound(path_to_file + 'audio-' + 'SELF-DESTRUCT_SEQUENCE_INITIATED' + '.mp3')



#this is the main function that gets used and to be added onto going forword
def allow_acsess():
	self_destruct = False
	os_speak.string(output_c + ' is authorized to use this program')
	os_speak.string('Hello, ' + output_c)
	time.sleep(3)
	print('\n')
	os_speak.string("I'm a new programe so I can't do to much but I can do simpal math, but I don't like it so I may be a little agressive")
	time.sleep(2)
	options = ['calculator', 'find variable']
	os_speak.string(str(options) + ' are all I can do at the moment' )
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
	allow_acsess() 
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
				aa = True
				output_c= f'{(first_name)} {(last_name)}'
				attemps = attemps + 70
		while attemps == 5:
			self_destruct = False 

#this is to maybe scare the unauthorized user index1 was prev deffinded in the begining of the code
if self_destruct == True: #play a sound and shuts down the device
	os_speak.string(output_c + ' is not authorized to use this program')
	print('SELF-DESTRUCT SEQUENCE INITIATED')
	os_speak.count_down('false',6)
	print(datetime.now())
	allow_acsess= False
	while index1 > 0: #this counts down 
		print('in '+ str(index1) +' seconds')
		os_speak.count_down('true',index1)
		time.sleep(1)
		index1 = index1 - 1
		while index1 == 1: # when index1 is equle to 1 it waits one sec and say's boom
			print('in 1 second')
			os_speak.count_down('true',index1)
			time.sleep(1)
			os_speak.ohno()#this will play a exploshion sound as long as its in the same folder
			time.sleep(1)
			index1 = index1 -1 
#			call(['shutdown','-h','now']) #this uses the call fuction to tell the computer to shutdown, you can comment it out if you want 


