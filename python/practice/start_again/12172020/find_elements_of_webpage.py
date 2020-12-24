#Get the elements from a page 
import requests
import bs4
res = requests.get("https://en.wikipedia.org/wiki/Nana_Akufo-Addo")
#print (res.text)
soup = bs4.BeautifulSoup(res.text,'lxml')
#print (soup)
print ("Get Title : {}".format(soup.select('title')[0].getText()))
first_item = soup.select('.toctext')[0]
#print (first_item)
for item in soup.select('.toctext') :
    print (item.text)