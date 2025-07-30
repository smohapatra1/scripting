#   https://www.geeksforgeeks.org/python/python-json-to-list/

import json
import pandas as pd

string = '{"name" : ["sam", "dam" , "kam", "plm" ]}'
dataFrame = pd.read_json(string)
print (type(string))
print (list(dataFrame["name"]))
print (type(list(dataFrame["name"])))
