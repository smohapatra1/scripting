#   https://www.geeksforgeeks.org/convert-python-list-to-json/

import json
list1 = [ 1, 2, 3, 'four', 'five']
print (type(list1))
print ("List1: ", list1)
json_str = json.dumps(list1)
print (type(json_str))
print ("Json List", json_str)