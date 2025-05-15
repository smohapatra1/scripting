#   https://www.geeksforgeeks.org/convert-class-object-to-json-in-python/

import json
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def to_dict(self):
        return {'name': self.name, 'age': self.age}
p1 = Person("Sam", 30)
res = json.dumps(p1.to_dict())
print (res)