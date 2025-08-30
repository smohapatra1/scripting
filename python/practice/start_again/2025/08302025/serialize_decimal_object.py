#   https://www.geeksforgeeks.org/python/python-json-serialize-a-decimal-object/

import json
from decimal import Decimal

decimal_num = Decimal(123.456)
def decimal_serial(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Type not serializable")
json_data = json.dumps(decimal_num, default=decimal_serial)
print(type(decimal_num))
print(type(json_data))
print(json_data)