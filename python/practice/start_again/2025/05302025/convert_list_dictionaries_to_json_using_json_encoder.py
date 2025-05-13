#   https://www.geeksforgeeks.org/python-convert-list-of-dictionaries-to-json/

import json

data = [
    {"id": ("1", "2", "3"), "name": ("bhanu", "sivanagulu"), "department": ("HR", "IT")},
    {"id": ("4", "5", "6"), "name": ("sai", "poori"), "department": ("HR", "IT")},
    {"id": ("7", "8", "9"), "name": ("teja", "gowtam"), "department": ("finance", "IT")},
    {"id": ("10", "11", "12"), "name": ("sai", "jyothi"), "department": ("business", "IT")},
    {"id": ("13", "14", "15"), "name": ("prudhvi", "nagendram"), "department": ("business", "IT")}
]

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, tuple):
            return list(obj)
        return super().default(obj)
json_result = json.dumps(data, cls=CustomEncoder, indent=2)
print (json_result)