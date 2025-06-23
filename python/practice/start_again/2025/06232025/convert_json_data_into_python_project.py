#   https://www.geeksforgeeks.org/python/convert-json-data-into-a-custom-python-object/

import json 
from collections import namedtuple

data = '{"name" : "SAMA", "id" : 1, "location" : "Ind"}'
x = json.loads(data, object_hook=lambda d:namedtuple("X", d.keys())(*d.values()))
print (x.name, x.id, x.location)

