#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

url_va = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
req_va = requests.get(url_va) #get contents of the website
soup = BeautifulSoup (req_va.content , "html.parser") #turn into soup object to manipulate in python

#find 'tr' tags with class 'election_
soup.find('table')
tags = soup.find_all('tr', 'election_item')

year = [] #create year list
for t in tags:
    year.append(t.contents[1].text) #append list

ELECTION_ID = [] #create election ID list
for i in range(len(tags)):
    ELECTION_ID.append(tags[i]["id"][-5:]) #append list

#print(year, Election_ID)
