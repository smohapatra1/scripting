#   https://www.geeksforgeeks.org/replace-multiple-lines-from-a-file-using-python/

import tempfile
import shutil

def approach(filename, old_lines, new_lines):
    updated_lines = []
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, start=1):
            for old, new in zip(old_lines, new_lines):
                line = line.replace(old, new)
            temp_file.write(line.encode())
            updated_lines.append(line.strip())
    temp_file.close()
    shutil.move(temp_file.name, filename)
    return updated_lines

old_lines = ["i am doing good"]
new_lines = ["i am doing very good"]
res = approach('file.txt', old_lines, new_lines)
for line in res:
    print (line)
with open('file,txt', 'w') as f:
    for line in res:
        f.write(line + '\n')



