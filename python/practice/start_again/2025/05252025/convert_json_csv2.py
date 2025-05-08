#   https://www.geeksforgeeks.org/convert-json-to-csv-in-python/

import json
import csv

with open('file.json') as f:
    jd = json.load(f)

df = open('json.csv', 'w', newline='')
cw = csv.writer(df)
c = 0 
for data in jd:
    if c == 0 :
        header = data.keys()
        cw.writerow(header)
        c += 1
    cw.writerow(data.values())
df.close()
