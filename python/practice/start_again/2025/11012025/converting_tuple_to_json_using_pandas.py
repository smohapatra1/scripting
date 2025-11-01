#   https://www.geeksforgeeks.org/python/convert-tuple-to-json-array-in-python/

import json
import pandas as pd

physics_tuple = ('Class 9', 'Physics', 'Laws of Motion',
                 ['Introduction', 'Newton First Law'])
df = pd.DataFrame([physics_tuple], columns=['Class', 'Subject', 'Topic', 'Subtopics'])

json_data = df.to_json(orient='records')
print (type(json_data))
print (json_data)