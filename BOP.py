input1= input('How may i help you?')
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
#nice
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_ele = soup.select('.r a')
linkTo0pen = min(5, len(link_ele))
for i in range(linkTo0pen):
    webbrowser.open('https://google.com'+ link_ele[i].get('href'))
