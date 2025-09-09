#   https://www.geeksforgeeks.org/python/parsing-json-nested-dictionary-using-python/

import json
from jsonpath_ng import jsonpath, parse

json_data = '{"name": "John", "age": 30, "address": {"city": "New York", "zipcode": "10001"}}'
parsed_data = json.loads(json_data)
jsonpath_Expr = parse('$.address.city')
match = jsonpath_Expr.find(parsed_data)
if match:
    print ('City:', match[0].value)
