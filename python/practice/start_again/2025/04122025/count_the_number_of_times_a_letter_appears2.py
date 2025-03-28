#   https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

def CounterLetter(FileName, letter):
    file = open('file.txt', 'r')
    text = file.read()
    count = 0 
    for word in text:
        if word == letter:
            count +=1
    return count

print (CounterLetter('file.txt', 'g' ))