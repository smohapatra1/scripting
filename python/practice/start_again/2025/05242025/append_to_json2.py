#   https://www.geeksforgeeks.org/append-to-json-file-using-python/

import json 

def write_json(new_data, filename='file.json'):
    with open(filename, "r+") as f:
        file_data = json.load(f)
        file_data["emp_details"].append(new_data)
        f.seek(0)
        json.dump(file_data, f, indent=4)
y = {"emp_name":"sam",
     "email": "s@abc.com",
     "job_profile": "Full Time"
    }

write_json(y)

