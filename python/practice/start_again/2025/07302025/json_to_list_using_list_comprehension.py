#   https://www.geeksforgeeks.org/python/python-json-to-list/

import json
string = '[{"name": "SAM", "sub" : "chem", "code" : "java"}]'
list1 = json.loads(string)
list2 = [ i for i in list1[0] ]
print (type(string))
print (list2)
print (type(list2))
