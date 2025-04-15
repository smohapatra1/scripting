#   https://www.geeksforgeeks.org/change-case-of-all-characters-in-a-txt-file-using-python/

with open('file.txt', 'r') as f1:
    with open('file2.txt', 'a') as f2:
        for line in f1:
            word_list = line.split()
            word_list = [word[0].upper() + word[1:].lower() if word else word for word in word_list]
            f2.write(" ".join(word_list) + "\n")