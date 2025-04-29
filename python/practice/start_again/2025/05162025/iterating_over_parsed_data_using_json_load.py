#   https://www.geeksforgeeks.org/json-loads-in-python/

import json

e = '{"id": "09", "name": "sam", "dept": "eng"}'
e_dict = json.loads(e)
for key in e_dict:
    print (key, ":", e_dict[key])
