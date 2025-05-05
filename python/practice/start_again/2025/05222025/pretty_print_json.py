#   

import json

dictionary ='{"id":"09", "name": "Nitin", "department":"Finance"}'
emp = json.loads(dictionary)

print (json.dumps(emp, indent=4, sort_keys=True))

