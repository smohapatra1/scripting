#   https://www.geeksforgeeks.org/python-pretty-print-json/

import json
import pprint

with open('file.json', 'r') as f:
    res = json.load(f)
    print (res)
    print ('\n')
pp = pprint.PrettyPrinter(indent=2, width=30, compact=True)
pp.pprint(res)