#   https://www.geeksforgeeks.org/python/how-to-build-a-simple-auto-login-bot-with-python/

from selenuim import webdriver
import os

def startBot(username, password, url):
    path = "C:\\Users\\hp\\Downloads\\chromedriver"
    driver = webdriver.Chrome(path)
    driver.get(url)
    driver.find_element_by_name("id/class/name of username").send_keys(username)
    driver.find_element_by_css_selector("id/class/name/css selector of login button").click()

username = "Enter your username"
password = "Enter your password"
url = "Enter the URL of login page of website"
startBot(username, password, url)

