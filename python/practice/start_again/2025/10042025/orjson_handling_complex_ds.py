#   https://www.geeksforgeeks.org/python/orjson-library-in-python/

import orjson
complex_data = {
    "user": {"id": 123, "username": "example_user"},
    "posts": [{"id": 1, "content": "Hello, world!"}, {"id": 2, "content": "Orjson is awesome!"}]
}
json_data = orjson.dumps(complex_data)
print (json_data)