#get the book with 2+ star rating 
import requests
import bs4
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
name = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(name.text,'lxml')
print ("Title {}".format(soup.select('title')[0].getText()))
product = soup.select('.product_pod')
#print (product)
example=product[0]
#print ("Get the rating {}".format(example.select('.star-rating.Three')))
print ("Title : {}".format(example.select('a')[1]['title']))
two_star_list = []
for n in range(1,3):
    scarp_url = base_url.format(n)
    res = requests.get(scarp_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Three')) != 0 :
            book_title = book.select('a')[1]['title']
            two_star_list.append(book_title)
print (two_star_list)
