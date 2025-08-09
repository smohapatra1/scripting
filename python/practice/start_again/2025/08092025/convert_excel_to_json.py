#   https://www.geeksforgeeks.org/python/convert-excel-to-json-with-python/

import pandas as pd
import json

data = pd.read_excel("test.xlsx", sheet_name="test1")
json_data = data.to_json()
print (json_data)