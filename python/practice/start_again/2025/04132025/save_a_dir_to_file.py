#   https://www.geeksforgeeks.org/save-a-dictionary-to-a-file/

try:

    dictionary = {'geek': 1, 'supergeek': True, 4: 'geeky'} 
    file = open('file.txt', 'wt')
    file.write(str(dictionary))
    file.close()
except:
    print ("Unable to write to file")
