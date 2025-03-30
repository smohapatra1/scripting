#   https://www.geeksforgeeks.org/save-a-dictionary-to-a-file/

import pickle


dictionary = {'geek': 1, 'supergeek': True, 4: 'geeky'}
try:
    file = open('file.txt', 'wb')
    pickle.dump(dictionary, file)
    file.close()
except:
    print ("Something went wrong")