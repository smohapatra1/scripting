#   https://www.geeksforgeeks.org/python/how-to-parse-json-from-bytes-in-python/

import json 

json_data = b'{"name": "Amit", "age": 30, "city": "Delhi"}'
decoded_data = json_data.decode('utf-8')
parsed_json = json.loads(decoded_data)
print (parsed_json)
