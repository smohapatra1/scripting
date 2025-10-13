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
json_data=json.dumps(data, indent=2)
print (json_data)