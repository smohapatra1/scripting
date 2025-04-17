#   https://www.geeksforgeeks.org/python-program-to-count-the-number-of-blank-spaces-in-a-text-file/

file = open ('file.txt', 'r')
count = 0 
while True:
    char = file.read(1)
    if char == " ":
        count += 1
    if not char:
        break
print (count)