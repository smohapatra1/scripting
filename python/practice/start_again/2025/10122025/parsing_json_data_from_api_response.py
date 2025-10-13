#   https://www.geeksforgeeks.org/python/how-to-parse-json-from-bytes-in-python/

import json
import urllib.request
url = 'https://jsonplaceholder.typicode.com/posts/1'
response = urllib.request.urlopen(url)
json_data_api = response.read()
decode_data_api = json_data_api.decode('utf-8')
parsed_json_api = json.loads(decode_data_api)
user_id = parsed_json_api['userId']
title = parsed_json_api['title']
body = parsed_json_api['body']
print ("UserId = ", user_id)
print ("Title  = ", title )
print ("Body   = ", body)