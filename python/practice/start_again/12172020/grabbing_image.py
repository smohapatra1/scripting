#grabbing an image 
import requests
import bs4
image = requests.get("https://en.wikipedia.org/wiki/Table_(furniture)")
soup = bs4.BeautifulSoup(image.text,'lxml')
print (soup)
print ("Title :{}".format(soup.select('title')[0].getText()))
print ("Paragraph : {}".format(soup.select('p')[0].getText()))
#print ("Get Images: {} ".format(soup.select('.thumbimage')))
image2 = soup.select('.thumbimage')[0]
print (image2['src'])
image_link = requests.get('https:' + image2['src'])
print (image_link)
#Download the image 
f = open("file.jpeg", "wb")
f.write(image_link.content)
f.close()
#print ("Get Source: {}".format(soup.select('.thumbimage')['src']))
