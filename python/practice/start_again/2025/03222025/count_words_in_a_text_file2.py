#   https://www.geeksforgeeks.org/python-program-to-count-words-in-text-file/

count = 0 
with open('file.txt', 'r') as f:
    data = f.read()
    lines = data.split(' ')
    for word in lines:
        if not word.isnumeric():
            count +=1
print ("Number of words are : ", count)