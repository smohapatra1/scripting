#   https://www.geeksforgeeks.org/python-program-to-capitalize-the-first-letter-of-every-word-in-the-file/


result = ""
file = open('file.txt', 'r')
for line in file:
    g = line.split()
    for elem in g:
        if len(result) > 0:
            result = result + " " + elem.strip().capitalize()
        else:
            result = elem.capitalize()
print (result)