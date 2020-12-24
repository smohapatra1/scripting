#Check your send and read emails
import smtplib
smtp_obj = smtplib.SMTP('smtp.gmail.com','587')
print (smtp_obj.ehlo())
import getpass
email = getpass.getpass('Enter your email: ')
password = getpass.getpass('Enter your password : ')
smtp_obj.login(email,password)
#Sending an email
from_address = email
to_address = email
subject = input("Enter the subject line: ")
message = input("Enter the body message : ")
msg = "subject: "+subject+'\n'+message 
smtp_obj.sendmail(from_address, to_address, msg)
smtp_obj.quit()