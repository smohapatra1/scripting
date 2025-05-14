#   https://www.geeksforgeeks.org/how-to-return-a-json-object-from-a-python-function/

import json

def test():
    lang = "python"
    company = "test"
    item = 1 
    price = 0.00
    value = {
        "language" : lang,
        "comp" : company,
        "items" : item,
        "prices" : price
    }
    return json.dumps(value)
print (test())