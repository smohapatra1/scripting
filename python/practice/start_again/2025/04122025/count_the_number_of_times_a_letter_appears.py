#   https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

def letterfreq(fileName, letter):
    file = open(fileName, 'r')
    text = file.read()
    return text.count(letter)

print (letterfreq('file.txt', 'g'))