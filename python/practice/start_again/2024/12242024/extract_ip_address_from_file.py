#   https://www.geeksforgeeks.org/extract-ip-address-from-file-using-python/

import re 

filepath = open("/Users/sam/test.txt", "r")
# with filepath as file :
#     fstring = file.readlines()
contents = filepath.readlines()
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') 
lst = []
for line in contents:
    lst.append(pattern.search(line)[0])
print (lst)