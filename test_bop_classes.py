from subprocess import *

from datetime import datetime
import playsound
from gtts import gTTS
import os 
import random 
import platform 
from class_calc_test import * 

if(platform.system() == 'Windows'):
	call(["cls"],shell=True)
elif(platform.system() == 'Linux'):
	call(["clear"],shell=True)
	call(["amixer", "-D", "pulse", "sset", "Master", "70%","on"],shell = True) #this is used to run a command to set the master volume to 70%

Test = True
path_to_file = '/home/kevin/Documents/bop-main/dep/'
#these is so when we use the os_speak.string we can hear what it says 
waitTime = 3

#prerequisites 

#var to be used later
attemps = 1
index1 = 6
#classes used later
def leave():
	print("")
class os_speak:#this class is used to make the computer talk and play sounds
	def __init__(self):
		self.audio_string = str()
	def string(astring):# a method to make the computer say someathing 
		audio_string = astring
		tts = gTTS(text=audio_string, lang='en')
		r = random.randint(1, 1000000)
		audio_file = 'audio-' + str(r) + '.mp3'
		tts.save(audio_file)
		print(audio_string +"\n")
		playsound.playsound(audio_file)
		os.remove(audio_file)
	def path(file):# a method to play a single file
		#print('assume the file was played')
		playsound.playsound(file)
	def ohno():# a method to make the computer go "boom"
		print('ohno')
		path = '/home/kevin/Documents/bop-main/dep/'
		playsound.playsound(path + 'battle003.mp3')
	def count_down(bool,num):#this is used in self_destruct just so the code is a little more readbule
		 print('')
		 if bool == True:
			 playsound.playsound(path_to_file + 'audio-' + str(num) + '.mp3')
			 
		 elif bool == False:
			 
			 playsound.playsound(path_to_file + 'audio-' + 'SELF-DESTRUCT_SEQUENCE_INITIATED' + '.mp3')
	def var(audio_string):#a method to make the computer ask a quesion and return an ansewr
		tts = gTTS(text=audio_string, lang='en')
		r = random.randint(1, 1000000)
		audio_file = 'audio-' + str(r) + '.mp3'
		tts.save(audio_file)
		playsound.playsound(audio_file)
		os.remove(audio_file)
		var = input(audio_string).strip(' ')
		return var


#this is the main function that gets used and to be added onto going forword
class access:
	def granted():
		
		os_speak.string(output_c + ' is authorized to use this program')
		os_speak.string('Hello, ' + output_c)
		time.sleep(waitTime)
		print('\n')
		os_speak.string("I'm a new programe so I can't do to much but I can do simpal math, but I don't like it so I may be a little agressive")
		time.sleep(waitTime)
		options = ['calculator', 'find variable','simon says']
		os_speak.string(str(options) + ' are all I can do at the moment' )
		want= os_speak.var('For ' + str(options[:1]) +' type "cal" or for ' + str(options[1:3]) + 'just type var\n')
		#a simpale calculator 
		
		if want == 'cal':
			calcculator.cal()
		#This is to find the varibule
		elif want == 'var':
			calcculator.var()
		elif want == 'simon says':
			speak = os_speak.var('what would you like me to say?')
			os_speak.string(speak)
		elif want == 'quit':
			leave()
		else:
			want = input("I'm sorry, I don't understand. Is their something less complex I may help with?")

	def denied():
		index1 = 6
		os_speak.string(output_c + ' is not authorized to use this program')
		print('SELF-DESTRUCT SEQUENCE INITIATED')
		os_speak.count_down(False,6)
		print(datetime.now())
		#allow_acsess= False
		while index1 > 0: #this counts down 
			print('in '+ str(index1) +' seconds')
			os_speak.count_down(True,index1)
			time.sleep(1)
			index1 = index1 - 1
			while index1 == 1: # when index1 is equle to 1 it waits one sec and say's boom
				print('in 1 second')
				os_speak.count_down(True,index1)
				time.sleep(1)
				os_speak.ohno()#this will play a exploshion sound as long as its in the same folder
				time.sleep(1)
				index1 = index1 -1 
#				call(['shutdown','-h','now']) #this uses the call fuction to tell the computer to shutdown, you can comment it out if you want 
				Test=False
				pass
while Test != False:
	waitTime =0
	first_name = "Kevin"
	last_name = "Hill"
	output_c= (first_name) + ' '+ (last_name)
	
	access.granted()

#this is to maybe scare the unauthorized user index1 was prev deffinded in the begining of the code

