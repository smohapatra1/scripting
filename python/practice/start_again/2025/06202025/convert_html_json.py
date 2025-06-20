#   https://www.geeksforgeeks.org/convert-html-source-code-to-json-object-using-python/

import xmltojson
import json
import requests

url = "https://geeksforgeeks-example.surge.sh"
Headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

html_response = requests.get(url=url, headers = headers)

with open("file.html", 'w') as html_file:
    html_file.write(html_response.text)
with open("file.html", "r") as html_file:
    html = html_file.read()
    json_ = xmltojson.parse(html)

with open("test.json", 'w') as file:
    json.dump(json_, file)

print (json_)