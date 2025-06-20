#   https://www.geeksforgeeks.org/python/how-to-compare-json-objects-regardless-of-order-in-python/

import json

json_1 = '{"Name":"GFG", "Class": "Website", "Domain":"CS/IT", "CEO":"San"}'

json_2 = '{"CEO":"San", "Domain":"CS/IT","Name": "GFG","Class": "Website"}'

json_dict1 = json.loads(json_1)
json_dict2 = json.loads(json_2)

print (sorted(json_dict1.items()) == sorted(json_dict2.items()))