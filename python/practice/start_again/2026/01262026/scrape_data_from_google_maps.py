#   https://www.geeksforgeeks.org/web-scraping/how-to-scrape-data-from-google-maps-using-python/

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome(
    executable_path="User\chromedriver_win32\chromedriver.exe", 
  options=options)

url = ["https://www.google.com/maps/place/%5CPapa+John's+Pizza/@40.7936551,-74.0124687,17z/data=!3m1!4b1!\
4m5!3m4!1s0x89c2580eaa74451b:0x15d743e4f841e5ed!8m2!3d40.\7936551!4d-74.0124687", "https://www.google.com/maps/place/%5CLucky+Dhaba/@30.653792,76.8165233,17z/data=!3m1!4b1!4m5!3m4!\
1s0x390feb3e3de1a031:0x862036ab85567f75!8m2!3d30.653792!4d76.818712"]
i = 0 

for i in range(len(url)):

    # Open the Google Map URL
    browser.get(url[i])

    # Obtain the title of that place
    title = browser.find_element_by_class_name(
        "x3AX1-LfntMc-header-title-title")
    print(i+1, "-", title.text)

    # Obtain the ratings of that place
    stars = browser.find_element_by_class_name("aMPvhf-fI6EEc-KVuj8d")
    print("The stars of restaurant are:", stars.text)
    print("\n")