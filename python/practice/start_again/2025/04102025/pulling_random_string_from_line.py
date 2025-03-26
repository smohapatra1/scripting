#   https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/

import random
with open('file.txt', 'r') as f:
    text = f.read()
    words = list(map(str, text.split()))
    print (random.choice(words))