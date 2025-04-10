#   https://www.geeksforgeeks.org/python-send-email-to-a-list-of-emails-from-a-spreadsheet/

import pandas as pd
import smtplib

my_email = 'xyz.gail.com'
password = '123456'

server = smtplib.SMTP_SSL('smtp.gmail.com', 456)
server.ehlo()
server.login(my_email, password)
email_list = pd.read_excel('test.xls')
names = email_list('NAME')
emails = email_list('EMAIL')

for i in range(len(emails)):
    name = names[i]
    message = "hello" + name
    server.sendmail(testmail.com, xyz.apple.com, test)
server.close()