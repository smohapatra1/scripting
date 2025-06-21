#   https://www.geeksforgeeks.org/python/convert-multiple-json-files-to-csv-python/

import pandas as pd

df1 = pd.read_json('file.json')
df2 = pd.read_json('file3.json')

print (df2)

df = pd.concat([df1, df2])
print (df)
df.to_csv("CSV.csv",index=False)
result = pd.read_csv("CSV.csv")
print (result)