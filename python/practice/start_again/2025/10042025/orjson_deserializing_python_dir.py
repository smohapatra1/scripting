#   https://www.geeksforgeeks.org/python/orjson-library-in-python/

import orjson
json_data = b'{"name":"Jane","age":25,"city":"Los Angeles"}'
python_object = orjson.loads(json_data)
print (python_object)