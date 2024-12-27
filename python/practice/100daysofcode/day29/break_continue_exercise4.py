#!/usr/bin/python
my_str = "university"
count = 0
for char in my_str:
    if char == "i":
        continue
    else:
        count = count + 1
print(count)
