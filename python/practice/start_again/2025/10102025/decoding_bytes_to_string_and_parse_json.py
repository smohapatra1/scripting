#   https://www.geeksforgeeks.org/python/how-to-parse-json-from-bytes-in-python/

import json

json_data = b'{"name": "Ankit", "age": 30, "city": "Mumbai"}'
decoded_json=json_data.decode('utf-8')
parsed_json=json.loads(decoded_json)
name = parsed_json['name']
age = parsed_json['age']
city = parsed_json['city']
print ("Name :", name)
print ("Age  :", age )
print ("City :", city )