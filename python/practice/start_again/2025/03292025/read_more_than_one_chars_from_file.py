#   https://www.geeksforgeeks.org/python-program-to-read-character-by-character-from-a-file/

with open('file.txt', 'r') as f:
    while True:
        c = f.read(5)
        if not  c:
            break
        print (c)
f.close()