#   https://www.geeksforgeeks.org/read-json-file-using-python/

import json
j_string = '{"name" : "sam1", "lang" : "eng"}'
y = json.loads(j_string)
print ("JSON string", y)