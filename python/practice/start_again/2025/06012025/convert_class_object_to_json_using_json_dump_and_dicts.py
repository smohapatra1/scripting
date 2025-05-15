#   https://www.geeksforgeeks.org/convert-class-object-to-json-in-python/

import json
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
p1 = Person("Sam", 40)
res = json.dumps(p1.__dict__)
print (res)