#   https://www.geeksforgeeks.org/how-to-keep-old-content-when-writing-to-files-in-python/

file = open('file.txt', 'a+')
file.seek(0)
content = file.read()
print (content)
content = "\n\n This is the new line \n\n"
file.write(content)
file.close()