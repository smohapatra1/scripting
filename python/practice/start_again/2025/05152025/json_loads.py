#   https://www.geeksforgeeks.org/json-loads-in-python/

import json
s = '{"Lang": "Python", "Verion": "10.x" }'
p = json.loads(s)
print (p)