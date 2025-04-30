#   https://www.geeksforgeeks.org/json-dumps-in-python/

import json
Dictionary ={1:'Welcome', 2:'to',
            3:'Geeks', 4:'for',
            5:'Geeks'}

json_string = json.dumps(Dictionary)

print('Equivalent json string of input dictionary:', json_string)
print("        ")
print(type(json_string))