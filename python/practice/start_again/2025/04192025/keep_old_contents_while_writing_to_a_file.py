#   https://www.geeksforgeeks.org/how-to-keep-old-content-when-writing-to-files-in-python/

file = open('file.txt', 'a')
content = "\n\n # this is the new line "
file.write(content)
file.close()