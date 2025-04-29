#   https://www.geeksforgeeks.org/tag/python-json/
#   https://www.geeksforgeeks.org/convert-csv-to-json-using-python/

import csv
import json

def make_json(csvFile, JsonFile):
    data = {}
    with open(csvFile, encoding='utf-8') as csv:
        csvReader = csv.DictReader(csv)
        for rows in csvReader:
            key = rows['No']
            data[key] = rows
    with open(JsonFile, 'w', encoding='utf-8') as json:
        json.write(json.dumps(data, indent=4))
csvFile = r'file.csv'
JsonFile = r'file.txt'
make_json(csvFile, JsonFile)
