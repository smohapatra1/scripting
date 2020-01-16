my_list = ["pet" ,"dog", 35, "cat", 23]
count = 0
for item in my_list:
    if type(item)== str:
        continue
    count = count + 1
print(count)
