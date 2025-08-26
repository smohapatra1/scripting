#   https://www.geeksforgeeks.org/python/how-to-convert-json-to-excel-in-python/

import json
import pandas as pd
data = json.load('file.json')
df = pd.DataFrame([data], index=0)
print (df)