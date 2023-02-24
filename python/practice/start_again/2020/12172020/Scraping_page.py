#Scraping a page 
import requests
import bs4
result = requests.get("https://www.google.com/?client=safari") 
type(result)
requests.models.Response
#print (result.text)
soup = bs4.BeautifulSoup(result.text,'lxml')
#print (soup)
#Return Paragraph 
print ("Return Paragraph {} : " .format(soup.select('p')))
print ("Return Paragraph with a keyword : {} ".format(soup.select('p')[0].getText))
#Return Title
print ("Return Title : {}".format(soup.select('title')[0].getText()))
#print (soup.select('title'))