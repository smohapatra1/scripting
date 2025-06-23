#   https://www.geeksforgeeks.org/python/serialize-and-deserialize-complex-json-in-python/

from typing import List
import json

class Student(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
class Team(object):
    def __init__(self, students: List[Student]):
        self.students = students
student1 = Student(first_name="SAM", last_name="MOH")
student2 = Student(first_name="SAM1", last_name="MOH1")
team = Team(students=[student1, student2])
json_data = json.dumps(team, default=lambda o:o.__dict__, indent=4)
print (json_data)

decoded_team = Team(**json.loads(json_data))
print (decoded_team)