#   https://www.geeksforgeeks.org/reading-and-writing-lists-to-a-file-in-python/

l = ['Geeks','for','Geeks!']

with open ('file.txt', 'w+') as f:
    for items in l:
        f.write('%s\n' % items)
    print ('File written successfully')