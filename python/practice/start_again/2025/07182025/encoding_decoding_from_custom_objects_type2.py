#   https://www.geeksforgeeks.org/python/encoding-and-decoding-custom-objects-in-python-json/

import json 
from json import JSONEncoder

class Student:
    def __init__ (self, name, roll_no, address):
        self.name = name
        self.roll_no = roll_no
        self.address = address
class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin
class EncodeStudent(JSONEncoder):
        def default(self, o):
            return o.__dict__

address = Address("Sam", "Adarsh", "203001")
student = Student("Raju", 53, address)

student_JSON = json.dumps(student, indent = 4,
                          cls = EncodeStudent)
print(student_JSON)
print(type(student_JSON))

student = json.loads(student_JSON)
print()
print(student)
print(type(student))