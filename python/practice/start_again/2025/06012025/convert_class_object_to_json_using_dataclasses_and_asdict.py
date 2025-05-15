#   https://www.geeksforgeeks.org/convert-class-object-to-json-in-python/

import json
from dataclasses import dataclass, asdict

@dataclass
class Person:
    name: str
    age: int
p1 = Person("Sam", 40)
res = json.dumps(asdict(p1))
print (res)