#   https://www.geeksforgeeks.org/python-program-to-replace-text-in-a-file/


s = input("Enter strings that has to be replaced : ")
f = open('fle.txt', 'r+')

f.truncate(0)
f.write(s)
f.close()
print ("Data has been replaced")