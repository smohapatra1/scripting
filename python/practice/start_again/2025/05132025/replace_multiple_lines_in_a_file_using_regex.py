#   https://www.geeksforgeeks.org/replace-multiple-lines-from-a-file-using-python/

import re

def approach(filename, old_lines, new_lines):
    with open(filename, 'r') as f:
        data = f.read()
        for old, new in zip(old_lines, new_lines):
            data = re.sub(re.escape(old), new, data)
        with open(filename, 'w') as f:
            f.write(data)
        res = data.split('\n')
        for line in res:
            print (line)

old_lines = ["i am doing good"]
new_lines = ["i am doing very good"]
approach('file.txt', old_lines, new_lines)