#   https://www.geeksforgeeks.org/python/how-to-parse-nested-json-in-python/

import pandas as pd 
import json
n_json = '{"employees": [{"name": "X", "age": 23}, {"name": "Y", "age": 22}]}'

data = json.loads(n_json)
df = pd.json_normalize(data, 'employees')
names = df['name']
ages = df['age']
print ("Names: ", list(names))
print ("Ages: ", list(ages))