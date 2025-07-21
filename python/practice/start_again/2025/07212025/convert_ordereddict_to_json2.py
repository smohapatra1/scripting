#   https://www.geeksforgeeks.org/python/how-to-convert-ordereddict-to-json/

from collections import OrderedDict
import json
od1 = OrderedDict([('1', 'one'), ('2', 'two')])
print (type(od1))
od1 = json.dumps(od1)
print (od1)