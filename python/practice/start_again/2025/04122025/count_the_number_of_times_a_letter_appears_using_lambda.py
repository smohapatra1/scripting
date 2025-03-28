#   https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

letterFreq = lambda fileName, letter: open(fileName, 'r').read().count(letter)

print (letterFreq('file.txt', 'g'))