#   https://www.geeksforgeeks.org/python-ways-to-convert-string-to-json-object/

import json
import ast
name = '{"Name": "sam", "age" : 20, "course": "read"}'
res = ast.literal_eval(name)
print (type(res), res)