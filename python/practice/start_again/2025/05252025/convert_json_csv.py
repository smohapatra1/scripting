#   https://www.geeksforgeeks.org/convert-json-to-csv-in-python/

import json
import csv

with open('file.json') as f:
    d = json.load(f)

ed = d['emp_details']
df = open('file.csv', 'w')
cw = csv.writer(df)
c = 0 
for emp in ed:
    if c == 0 :
        h = emp.keys()
        cw.writerow(h)
        c +=1
    cw.writerow(emp.values())
df.close()