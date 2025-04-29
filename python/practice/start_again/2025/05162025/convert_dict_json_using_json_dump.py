#   https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/

import json

d = {"name": "sam", "age": "20"}

files = [
    ("sample_default.json", {}),
    ("sample_pretty.json", {"indent": 4}),
    ("sample_sorted.json", {"sort_keys": True, "indent": 4}),
    ("sample_ascii.json", {"ensure_ascii": False, "indent": 4})

]

for filename, options in files:
    with open(filename, 'w') as f:
        json.dump(d, f, **options)

for _, options in files:
    print (json.dumps(d, **options))