#   https://www.geeksforgeeks.org/python-program-to-replace-text-in-a-file/

x = input("enter text to be replaced:")
y = input("enter text that will replace:")
with open('file.txt', 'r') as file:
    filedata = file.read()
    filedata = filedata.replace(x, y)
with open('file.txt', 'w') as file:
    file.write(filedata)
print("Data replaced Successfully")
