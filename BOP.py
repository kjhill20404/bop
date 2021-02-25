first_name= input('what is your first name!!!!!!?????:').lower().strip(' ')
last_name= input('what is your last name!!!!!!!!??????:').lower().strip(' ')
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

if input1.find('+ - x * /  ^'):
    input1 = input1.strip(' abcdefghijklmnopqrstuvwyz?'+ ' ')
    inNum = len(input1)
    # float isn't working and i need to find out why
    print(inNum) 
    if (input1).find('+'):
        input1 = input1.split()
        inNum = inNum-1 
        print(input1[::2])
        

    
#next step is to make a web scrapper to search google 
#everything below this was added on 11-6-2020 if not work use 'intro to web scraping with python ans brautiful soup' on youtube


import requests, sys, webbrowser, bs4

from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_ele = soup.select('.r a') #nice XD
linkTo0pen = min(5, len(link_ele))
for i in range(linkTo0pen):
