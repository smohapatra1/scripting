#   https://www.geeksforgeeks.org/python/encoding-and-decoding-custom-objects-in-python-json/

import json 

class Student:
    def __init__(self, name, roll_no, address):
        self.name = name
        self.roll_no = roll_no
        self.address = address
 
    def to_json(self):
        '''
        convert the instance of this class to json
        '''
        return json.dumps(self, indent = 4, default=lambda o: o.__dict__)
 
class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin

address = Address("S", "xyz", "203001")
student = Student("S", 53, address)
student_json = student.to_json()
print (student_json)
print (type(student_json))

student = json.loads(student_json)
print (student)
print (type(student))