#   https://www.geeksforgeeks.org/python/modify-json-fields-using-python/

import json
json_data = '{"name": "John", "age": 25, "city": "New York"}'
data['age'] = 26
modified_json = json.dumps(data)
print ("Before Modifying : ", json_data)
print ("After Modifying  : ", modified_json)