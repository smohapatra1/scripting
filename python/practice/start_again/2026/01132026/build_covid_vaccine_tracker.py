#   https://www.geeksforgeeks.org/python/build-a-covid19-vaccine-tracker-using-python/

import requests
from bs4 import BeautifulSoup

def getData(url):
    r = requests.get(url)
    return r.text
htmldata = getData("https://covid-19tracker.milkeninstitute.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
result = str(soup.find_all("div", class_="is_h5-2 is_developer w-richtext"))

print ("No 1 " + result[46:86])
print ("No 2 " + result [130:150])

