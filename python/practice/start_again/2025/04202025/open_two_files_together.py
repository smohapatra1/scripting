#   https://www.geeksforgeeks.org/how-to-open-two-files-together-in-python/

with open('file.txt') as f1 , open('file2.txt') as f2:
    print (f1.read())
    print (f2.read())
    f1.close()
    f2.close()