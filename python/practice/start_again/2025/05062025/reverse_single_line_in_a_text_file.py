#   https://www.geeksforgeeks.org/python-program-to-reverse-a-single-line-of-a-text-file/

f = open('file.txt', 'r')
lines = f.readlines()
f.close()
choice = 1 
line = lines[choice].split()
Reversed = ' '.join(line[::-1])
lines.pop(choice)
lines.insert(choice, Reversed)
u = open('file.txt', 'w')
u.writelines(lines)
u.close()