#   https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/

import random

print (random.choice(open('file.txt', "r").readline().split()))