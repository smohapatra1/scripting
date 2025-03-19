#   https://www.geeksforgeeks.org/python-program-to-replace-specific-line-in-file/

with open('file.txt', 'r') as file:
    data = file.readlines()
print (data)
data[1] = "Here is my new line \n"
with open('file.txt', 'w') as file:
    file.writelines(data)
print("Data replaced successfully")