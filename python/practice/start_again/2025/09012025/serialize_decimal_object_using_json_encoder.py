#   https://www.geeksforgeeks.org/python/python-json-serialize-a-decimal-object/

import json 
from decimal import Decimal

decimal_number = Decimal(1.234)
class Decimal_Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super().default(o)

json_data = json.dumps(decimal_number, cls=Decimal_Encoder)
print (type(decimal_number))
print (type(json_data))
print (json_data)
