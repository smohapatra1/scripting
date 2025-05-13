#   https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/

import json
from urllib.request import urlopen

url = "https://api.github.com"
response = urlopen(url)
data = json.loads(response.read())
print (data)