#   https://www.geeksforgeeks.org/convert-text-file-to-json-in-python/

import json

file = 'file.txt'
dict1 = {}
fields = ['name', 'designation', 'age', 'salary']

with open(file) as f:
    l = 1 
    for line in f:
         
        # reading line by line from the text file
        description = list( line.strip().split(None, 4))
        print(description) 
        sno ='emp'+str(l)
        i = 0
        dict2 = {}
        while i<len(fields):
                dict2[fields[i]]= description[i]
                i = i + 1
        dict1[sno]= dict2
        l = l + 1
    out_file = open('test2.json', 'w')
    json.dump(dict1, out_file, indent=4 )
    out_file.close()
