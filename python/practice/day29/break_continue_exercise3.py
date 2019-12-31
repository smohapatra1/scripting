#!/usr/bin/python
my_list = ["dog", 24, "cat", 12]
count = 0
for element in my_list:
    print (element)
    if element == "cat":
        continue
    count = count + 1
print(count)
