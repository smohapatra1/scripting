#   https://www.geeksforgeeks.org/python/serialize-and-deserialize-complex-json-in-python/

import json 
class GFG_User(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
user = GFG_User(first_name='Sam', last_name='Moh')
json_data = json.dumps(user.__dict__)
print (json_data)
print (GFG_User(*json.loads(json_data)))