
# https://www.geeksforgeeks.org/json-dumps-in-python/

import json

Dictionary ={(1, 2, 3):'Welcome', 2:'to',
            3:'Geeks', 4:'for',
            5:'Geeks', 6:float('nan')}


json_string = json.dumps(Dictionary, 
                         skipkeys = True, 
                         allow_nan = True,
                         indent = 6)

print('Equivalent json string of dictionary:',  json_string)