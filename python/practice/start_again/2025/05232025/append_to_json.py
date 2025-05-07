#   https://www.geeksforgeeks.org/append-to-json-file-using-python/

import json
d_string = '{"name" : "sam", "sex" : "male"}'
y = {"age": 20}
z = json.loads(d_string)
z.update(y)
print (json.dumps(z))