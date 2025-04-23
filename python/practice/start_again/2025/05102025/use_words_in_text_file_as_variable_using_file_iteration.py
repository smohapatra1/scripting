#   https://www.geeksforgeeks.org/how-to-use-words-in-a-text-file-as-variables-in-python/

with open('file.txt', 'r') as file:
    for line in file:
        word = line.strip()
        print (f"{word} SAMAR?")