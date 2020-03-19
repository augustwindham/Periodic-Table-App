
import requests
from bs4 import BeautifulSoup
import pandas as pd


print('getting data')
url = 'https://www.webelements.com/'


r = requests.get(url).content

with open('PThtml.txt','w') as pt: #saves pt html to file so i dont have to request
    pt.write(str(r))


with open(   'PThtml.txt','r')as PT:
    htm = PT.read()

soup = BeautifulSoup(htm, 'html.parser')
tb = soup.table.tbody

hrefs = []

for i in tb.findAll('a', href = True):
    hrefs.append(i['href'])
#print(hrefs)

table = []
for i in hrefs:

    r = requests.get(url+i).content
    sp = BeautifulSoup(r, 'html.parser')

    for h in sp.findAll('ul', {'class':'ul_facts_table'}):
        with open('PTdata.csv','a+') as file:

            for g in h.findAll('li'):
                file.write(g.text+',')
            file.write('\n')

                #print(g.text)



#make PT class and element class
#for each row of the pt pass element data to the element class
#populate grid with Main Data
#on click pull up popup
#make argument of gui file chance to use it like api
'''in other file'''
