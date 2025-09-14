#   https://www.geeksforgeeks.org/python/single-vs-double-quotes-in-python-json/

import json 
json_escape = '{"message" : "Hello, world!"}'
parsed_escape_chars  =json.loads(json_escape)
print ("Using double quotes with escape chars" )
print (parsed_escape_chars)