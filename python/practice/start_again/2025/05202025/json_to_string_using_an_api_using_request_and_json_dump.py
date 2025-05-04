#   https://www.geeksforgeeks.org/python-convert-json-to-string/

import json
import requests

res = requests.get('http://dummy.restapiexample.com/api/v1/employees')
d = json.loads(res.text)

d = json.dumps(d)

print (d)