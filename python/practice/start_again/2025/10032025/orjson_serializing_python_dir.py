#   https://www.geeksforgeeks.org/python/orjson-library-in-python/

import json
data_to_serialize = {"name": "Sama", "age": 30, "city": "San"}
json_data = orjson.dumps(data_to_serialize)
print (json_data)