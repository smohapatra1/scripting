#   https://www.geeksforgeeks.org/convert-python-list-to-json/

import json
class ListOfEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, list):
            return obj
        return json.JSONEncoder.default(self, obj)

data = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]
print (type(data))
json_output = json.dumps(data, cls=ListOfEncoder)
print (json_output)
print (type(json_output))
    