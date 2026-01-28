#   https://www.geeksforgeeks.org/python/scraping-weather-data-using-python-to-get-umbrella-reminder-on-email/

import schedule
import smtplib
import requests
from bs4 import BeautifulSoup

def Umbrella_Reminder():
    city = "Pune"
    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temperature = soup.find('div',
                            attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_sky = soup.find('div', 
                         attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    sky = time_sky.split('\n')[1]
    if sky == "Rainy" or sky == "Rain And Snow" or sky == "Showers" or sky == "Haze" or sky == "Cloudy":
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        smtp_object.starttls()
        
        # Authentication
        smtp_object.login("YOUR EMAIL", "PASSWORD")
        subject = "GeeksforGeeks Umbrella Reminder"
        body = f"Take an umbrella before leaving the house.\
        Weather condition for today is {sky} and temperature is\
        {temperature} in {city}."
        msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nGeeksforGeeks".encode(
            'utf-8')
        
        # sending the mail
        smtp_object.sendmail("FROM EMAIL",
                             "TO EMAIL", msg)
        
        # terminating the session
        smtp_object.quit()
        print("Email Sent!")
schedule.every().day.at("06:00").do(Umbrella_Reminder)

while True:
    schedule.run_pending()