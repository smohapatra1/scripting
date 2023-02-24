#Create a file 
import os 
import shutil
import send2trash
print (os.listdir())
f = open("practice.txt", 'w+')
f.write('Hello Samar')
f.close()
shutil.move('practice.txt', '/tmp')
print (os.listdir('/tmp/'))
#send2trash - Delete the file, sending to trash 
send2trash.send2trash('/tmp/practice.txt')



