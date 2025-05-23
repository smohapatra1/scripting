#   https://www.geeksforgeeks.org/pandas-convert-json-to-dataframe/

import json
import pandas as pd
data = {
    "0": "Sama",
    "1": "Sama2",
    "3": "Sama3"
}
with open('file.json', 'w') as f:
    json.dump(data, f, indent=4)
    