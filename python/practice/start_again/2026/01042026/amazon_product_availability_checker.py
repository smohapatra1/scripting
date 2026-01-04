#   https://www.geeksforgeeks.org/python/amazon-product-availability-checker-using-python/

from lxml import html
import requests
from time import sleep
import time
import schedule
import smtplib 

receiver_email_id = "EMAIL_ID_OF_USER"

def check(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url, headers=headers)
    for i in range(20):
        sleep (3)
        doc = html.fromstring(page.content)
        XPATH_AVAILABILITY = '//div[@id ="availability"]//text()'
        RAW_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
        AVAILABILITY = ''.join(RAW_AVAILABILITY).strip() if RAW_AVAILABILITY else None
        return AVAILABILITY
    
def send_email(ans, product):
    GMAIL_USERNAME = "GMAIL_ID"
    GMAIL_PASSWORD = "GMAIL_PASSWORD"
    recipient = receiver_email_id
    body = ans
    email_subject = product + 'Product Availability Status'
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                        "subject: " + email_subject,
                        "to: " + recipient,
                        "mime-version: 1.0",
                        "content-type: text/html"])
    content = headers + "\r\n\r\n" + body
    s.sendmail(GMAIL_USERNAME, recipient, content)
    print("Email sent to " + receiver_email_id)
    s.quit()
def ReadAsin():
    # Asin Id is the product Id which 
    # needs to be provided by the user
    Asin = 'B077PWK5BT' 
    url = "https://www.amazon.in/dp/" + Asin
    print ("Processing: "+url)
    ans = check(url)
    arr = [
        'Only 1 left in stock.',
        'Only 2 left in stock.',
        'In stock.']
    print(ans)
    if ans in arr:
        # sending email to user if 
        # in case product available 
        send_email(ans, Asin)

def job():
    print("Tracking....") 
    ReadAsin()
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
