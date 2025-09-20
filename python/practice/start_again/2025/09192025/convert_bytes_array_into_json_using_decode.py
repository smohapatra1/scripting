#   https://www.geeksforgeeks.org/python/convert-a-bytes-array-into-json-format-in-python/

import json
bytes_data = b'{"key": "value", "nested": {"inner_key": [1, 2, 3]}}'
print(type(bytes_data))
json_data = json.loads(str(bytes_data, 'utf-8'))
print (json_data)
print(type(json_data))