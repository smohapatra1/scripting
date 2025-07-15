#   https://www.geeksforgeeks.org/python/how-to-parse-data-from-json-into-python/

import json 
geek = '{"Name": "nightfury1", "Languages": ["Python", "C++", "PHP"]}'
dict = json.loads(geek)
print ("Dictionary after parsing :", dict)
print ("\n Values in languages : ", dict['Languages'])