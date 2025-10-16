#   https://www.geeksforgeeks.org/python/extract-nested-data-from-complex-json/
import json

data = {
    "location": {
        "country": "India",
        "state": "Uttar Pradesh",
        "city": "Greater Noida"
    },
    "organizations": [
        {
            "name": "GeeksforGeeks",
            "type": "Educational",
            "departments": ["Computer Science", "Mathematics", "Physics"]
        },
        {
            "name": "TechCorp",
            "type": "Technology",
            "departments": ["Software Development", "Hardware Design"]
        }
    ],
    "projects": {
        "ongoing": ["ProjectA", "ProjectB"],
        "completed": ["ProjectX", "ProjectY"]
    }
}

def extract_data_recursive(data, keys):
    return data[keys[0]] if len(keys) == 1 else extract_data_recursive(data[keys[0]], keys[1:])
edu_dept = extract_data_recursive(data, ["organizations", 0, "departments", 0])
print (f"Extracted Data using recursion : ")
print (f"Educational Dept Recursive : {edu_dept}")