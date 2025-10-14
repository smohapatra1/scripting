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
country_data = data["location"]["country"]
city_data = data["location"]["city"]

print (f"Extracted Data using Dot Notation: ")
print (f"Country: {country_data}")
print (f"City: {city_data}")