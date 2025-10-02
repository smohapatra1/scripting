#   https://www.geeksforgeeks.org/python/orjson-loads-vs-json-loads-in-python/

import orjson
import json
import time

with open('country.json') as f:
    data = json.load(f)

start_time = time.time()
decorated_data_json = json.loads(json.dumps(data))
end_time = time.time()
print (f"Time taken to decode JSON data using json.loads(): {end_time - start_time:.4f} seconds")
start_time = time.time()
decorated_data_orjson = orjson.loads(json.dumps(data))
end_time = time.time()
print (f"Time taken to decode JSON data using orjson.loads(): {end_time - start_time:.4f} seconds")
print (f"Decoded data is the same : {decorated_data_json == decorated_data_orjson}")

