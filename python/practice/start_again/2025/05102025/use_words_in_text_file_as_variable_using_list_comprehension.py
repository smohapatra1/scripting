#   https://www.geeksforgeeks.org/how-to-use-words-in-a-text-file-as-variables-in-python/

with open('file.txt', 'r') as f:
    words = [line.strip() for line in f]
for word in words:
    print (f"{word} Samar ?")