#   https://www.geeksforgeeks.org/how-to-use-words-in-a-text-file-as-variables-in-python/

with open('file.txt', 'r') as f:
    lines = f.readlines()
words = []
for line in lines:
    word = line.strip()
    words.append(word)
for word in words:
    print (f"{word} = Samar")
