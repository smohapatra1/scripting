#   https://www.geeksforgeeks.org/python/convert-a-bytes-array-into-json-format-in-python/

import json

bytes_data = b'{"key": "value", "nested": {"inner_key": [1, 2, 3]}}'
class complexDecoder(json.JSONDecoder):
    def decode(self, s, **kwargs):
        return super().decode(s, **kwargs)
print (type(bytes_data))
json_data = json.loads(bytes_data, cls = complexDecoder)
print (json_data)
print (type(json_data))
