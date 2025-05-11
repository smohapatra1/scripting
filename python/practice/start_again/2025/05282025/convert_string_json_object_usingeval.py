#   https://www.geeksforgeeks.org/python-ways-to-convert-string-to-json-object/
s = '{"name": "John", "age": 30, "city": "New York"}'

d = eval(s)
print (type(d), d)
