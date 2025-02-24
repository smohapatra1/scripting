#   https://www.geeksforgeeks.org/write-a-dictionary-to-a-file-in-python/

details={'Name' : "Alice", 
         'Age' : 21, 
         'Degree' : "Bachelor Cse", 
         'University' : "Northeastern University"} 

with open('file.txt', 'w') as f:
    for key, val in details.items():
        f.write('%s:%s\n' %(key, val))
