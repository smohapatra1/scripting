#   https://www.geeksforgeeks.org/python/difference-between-json-and-dictionary-in-python/

import json
a = '{"name": "Sam","age": "40", "city": "KA" }'
b = json.loads(a)
print (b["city"])