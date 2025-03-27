#   https://www.geeksforgeeks.org/find-the-most-repeated-word-in-a-text-file/

file = open('file.txt', 'r')
freq_word = ''
freq = 0 
words = []

for line in file:
    line_word = line.lower().replace(',','').replace('.','').split(" ")
    for w in line_word:
        words.append(w)
for i in range(0, len(words)):
    count = 1
    for j in range(i+1, len(words)):
        if (words[i] == words[j]):
            count = count + i 
    if count > freq:
        freq = count
        freq_word = words[i]
print ("Most repeated words : " + freq_word)
print ("Frequency           : " + str(freq))
file.close()