#   https://www.geeksforgeeks.org/python/desktop-notifier-python/

import requests
import xml.etree.ElementTree as ET
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"   

def loadRSS():
    resp=requests.get(RSS_FEED_URL)
    return resp.content
def parseXML(rss):
    root = ET.fromstring(rss)
    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}
        for child in item:
            if child.tag == '{https://video.search.yahoo.com/mrss':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        newsitems.append(news)
    return newsitems

def TopStories():
    rss = loadRSS()
    newsitems = parseXML(rss)
    return newsitems
