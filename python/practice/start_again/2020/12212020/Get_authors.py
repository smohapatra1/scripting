# Get Authors 

import requests
import bs4

res=requests.get('https://quotes.toscrape.com')
res2 = 'https://quotes.toscrape.com/page/{}/'

soup = bs4.BeautifulSoup(res.text,'lxml')
#print (soup)
title = soup.select('title')[0].getText()
print (title)
#subject=soup.select('.itemprop')[0]
author=soup.select('.author')
#print (subject)
#print(author)

authors = set()
for name in soup.select('.author'):
    #name2 = name.select('.itermprop')
    authors.add(name.text)
    #Print without list 
    print (name.text)
print (authors)
quotes = soup.select('.text')
get_quotes = []
for quote in quotes:
    get_quotes.append(quote.text)
    #Print without list 
    print (quote.text)
print (get_quotes)
tag = soup.select('.tag-item')
get_tags = []
for tags in tag:
    get_tags.append(tags.text)
    #Print without list 
    print (tags.text)
print (get_tags)

#getting through more pages 
auth_list=[]
for n in range(1,99999):
    quotes_url=res2.format(n)
    res3 = requests.get(quotes_url)
    soup2 = bs4.BeautifulSoup(res3.text,'lxml')
    authors = soup2.select('.author')
    for author in authors:
        print (author.text)
        if "No quotes found!" in author.text :
            print ("I am done")