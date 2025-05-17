#   https://www.geeksforgeeks.org/convert-class-object-to-json-in-python/

import json 

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def __json__(self):
        return {'name': self.name, 'age': self.age}

p1 = Person("sam", 30)
res = json.dumps(p1, default=lambda o:o.__json__() if hasattr(o, '__json__') else None)
print (res)