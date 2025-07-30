#   https://www.geeksforgeeks.org/python/python-json-to-list/

import json
string = "[1, 2, 3, 4]"
array = json.loads(string)
print (array)
print (type(string))
print (array[0])