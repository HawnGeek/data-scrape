#This script will illustrate how to call the BeautifulSoup daemon and scrape data from a website#

#import urllib2
import urllib.request
import requests as req
from bs4 import BeautifulSoup

#1 target web page:
web_page = 'https://finance.yahoo.com/quote/FB?p=FB'


#query the website and return the html to the variable page:

#windows only syntax for python 3.6.5
#page = urllib.request.Request(web_page)
#request = urllib.request.Request(web_page)
#response = urllib.request.urlopen(page)
#print (response.read().decode('utf-8'))

page = req.get(web_page)

soup = BeautifulSoup(page.text,'html.parser')

#print(soup) 

name_box = soup.find('h1', attrs={'class': 'D(ib)'})
#print(name_box)
name = name_box.text
print(name)

price_box = soup.find('span', attrs={'class': 'Fw(b)'})
price = price_box.text
print(price)

import csv
from datetime import datetime

with open('index.csv', 'a') as csv_file: 
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])

#notes for a while loop

#input = 0
#while input < 10:
    #print(input)
    #input = input + 1
    #input +=1





