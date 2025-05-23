#   https://www.geeksforgeeks.org/convert-python-list-to-json/

import json

data = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]
with open("file.json", "w") as f:
	json.dump(data, f)

# Download the file
f.download('file.json')