#   https://www.geeksforgeeks.org/python/modify-json-fields-using-python/

import json
json_data = '{"name": "Eva", "age": 28, "city": "Seattle"}'
data = json.loads(json_data)
data.update({"name": "Sam"})
modified_json = json.dumps(data)
print ("Before Modifications : ", json_data)
print ("After  Modifications : ", modified_json)