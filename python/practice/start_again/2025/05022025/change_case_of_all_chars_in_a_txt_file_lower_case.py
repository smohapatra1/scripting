#   https://www.geeksforgeeks.org/change-case-of-all-characters-in-a-txt-file-using-python/

with open('file.txt', 'r') as f:
    with open('file2.txt', 'a') as f2:
        # for line in f:
        f2.write(f.read().lower())
