#   https://www.geeksforgeeks.org/create-inverted-index-for-file-using-python/

dict = {}
for i in range(line):
    check = array[i].lower()
    for item in tokens_without_sw:
        if item in check:
            if item not in dict:
                dict[item] = []
            if item in dict:
                dict[item].append(i+1)

dict
