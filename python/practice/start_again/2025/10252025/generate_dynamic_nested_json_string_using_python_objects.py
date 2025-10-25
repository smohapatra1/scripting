#   https://www.geeksforgeeks.org/python/python-to-generate-dynamic-nested-json-string/

import json
class Person:
    def __init__(self, name, age, address, contacts):
        self.name = name
        self.age = age
        self.address = address
        self.contacts = contacts

person_obj = Person("Jane", 30, {"city": "Townsville", "zip": "54321"}, [{"type": "email", "value": "jane@example.com"}])

def serialize(obj):
    if isinstance(obj, Person):
        return obj.__dict__
    return obj
json_string_obj = json.dumps(person_obj, default=serialize, indent=2)
print("\nOutput")
print(json_string_obj)