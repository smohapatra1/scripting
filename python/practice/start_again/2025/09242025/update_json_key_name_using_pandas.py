#   https://www.geeksforgeeks.org/python/update-json-key-name-in-python/

import pandas as pd 
json1 = {'old_key1': 'value1', 'old_key2': 'value2'}
df = pd.DataFrame([json1])
df = df.rename(columns={'old_key1': 'new_key1', 'old_key2': 'new_key2'})
json2 = df.to_json(orient='records')[1:-1]
print (json2)