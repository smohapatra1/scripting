#   https://www.geeksforgeeks.org/python/saving-api-result-into-json-file-in-python/

import requests
import json
api_url = "http://localhost:8000/Hello-world"

response = requests.get(api_url)
if response.status_code == 200:
    new_data = response.json()
    try:
        with open("file.json", 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        existing_data = []
    existing_data.append(new_data)
    with open("data.json", 'w') as file2:
        json.dump(existing_data, file2, indent=4)
        print ("Data appended  to data.json file")
else:
    print ("Failed to retrieve  data from API. status code:", response.status_code)