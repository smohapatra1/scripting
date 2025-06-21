#   https://www.geeksforgeeks.org/python/how-to-compare-json-objects-regardless-of-order-in-python/

import json

json_1 = '{"Name":"GFG", "Class": "Website", "Domain":"CS/IT", "CEO":"Sandeep Jain","Subjects":["DSA","Python","C++","Java"]}'

json_2 = '{"CEO":"Sandeep Jain","Subjects":["C++","Python","DSA","Java"], "Domain":"CS/IT","Name": "GFG","Class": "Website"}'


json1_dict = json.loads(json_1)
json2_dict = json.loads(json_2)

def sorting(item):
    if isinstance(item, dict):
        return sorted((key, sorting(values)) for key, values in item.items())
    if isinstance(item, list):
        return sorted(sorting(x) for x in item)
    else:
        return item


print(sorting(json1_dict) == sorting(json2_dict))