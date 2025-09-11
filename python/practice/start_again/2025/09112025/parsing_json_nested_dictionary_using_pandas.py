#   https://www.geeksforgeeks.org/python/parsing-json-nested-dictionary-using-python/

import json
import pandas as pd 
json_data = '{"name": "John", "age": 30, "address": {"city": "New York", "zipcode": "10001"}}'
parsed_data = pd.json_normalize(json.loads(json_data))
print ('City:', (parsed_data['address.city'].values[0]))