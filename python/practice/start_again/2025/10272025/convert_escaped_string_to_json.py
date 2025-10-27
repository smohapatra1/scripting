#   https://www.geeksforgeeks.org/python/convert-escaped-string-to-json-in-python/

import json
import ast

escaped_string = '{"name": "John\\nDoe", "age": 25}'
unescaped_dist=ast.literal_eval(escaped_string)
json_data = json.dumps(unescaped_dist)
print (json_data)