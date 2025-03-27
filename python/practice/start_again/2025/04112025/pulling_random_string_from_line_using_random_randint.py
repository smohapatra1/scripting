#   https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/

import random

with open('file.txt', 'r') as f:
    data = f.read()
    words = data.split()
    word_pos = random.randint(0, len(words) - 1)
    print ("Position         :", word_pos)
    print ("word at position : ", words[word_pos])