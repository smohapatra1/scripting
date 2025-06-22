#   https://www.geeksforgeeks.org/python/convert-multiple-json-files-to-csv-python/

import pandas as pd
import json
with open('file.json') as file:
    data = json.load(file)

print (data)
df = pd.DataFrame(data['sample_data'])
print (df)
for i , item in enumerate(df['name']):
    df['location_city'] = dict(df['Location'])[i]['City']
    df['location_state'] = dict(df['Location'])[i]['State']
for i, item in enumerate(df['hobbies']):
    df['hobbies_{}'.format(i)] = dict(df['hobbies'])[i]

df = df.drop({'Location', 'hobbies'}, axis=1)
print (df)
df.to_csv("CSV.csv", index=False)
result = pd.read_csv("CSV.csv")
print (result)