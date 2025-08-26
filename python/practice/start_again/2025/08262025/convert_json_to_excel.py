#   https://www.geeksforgeeks.org/python/how-to-convert-json-to-excel-in-python/

import json
import pandas as pd

with open('file.json') as file:
    data = json.load(file)
print (data)