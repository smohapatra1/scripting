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

edu_dept = [dept for org in data["organizations"]
            if org["name"] == "GeeksforGeeks" for dept in org["departments"]]
completed_project = [ project for status, projects in data["projects"].items() if status == "completed" for project in projects]

print (f"Extracted data using list comprehension: ")
print (f"Educational Departments : {edu_dept}")
print (f"Completed projects : {completed_project}")
