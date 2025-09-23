#   https://www.geeksforgeeks.org/python/update-json-key-name-in-python/

import json

original_json = '{"old_key1": "value1", "old_key2": "value2"}'
json_data = json.loads(original_json)
json_data['new_key1'] = json_data.pop('old_key1')
json_data['new_key2'] = json_data.pop('old_key2')
updated_json = json.dumps(json_data)
print (updated_json)