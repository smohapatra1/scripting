import imaplib
import getpass
M = imaplib.IMAP4_SSL('imap.gmail.com')
email = getpass.getpass('Enter your email: ')
password = getpass.getpass("Enter your password: ")
M.login(email,password)
#Prints all the levels or folders 
M.list()
M.select('inbox')