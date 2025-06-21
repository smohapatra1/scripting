#   https://www.geeksforgeeks.org/python/how-to-compare-json-objects-regardless-of-order-in-python/

import json

json_1 = '{"Name":"GFG", "Class": "Website", "Domain":"CS/IT", "CEO":"Sandeep Jain","Subjects":["DSA","Python","C++","Java"]}'

json_2 = '{"CEO":"Sandeep Jain","Subjects":["C++"]}'

json1_dict = json.loads(json_1)
json2_dict = json.loads(json_2)

print(sorted(json1_dict.items()) == sorted(json2_dict.items()))

print(sorted(json1_dict.items()))
print(sorted(json2_dict.items()))