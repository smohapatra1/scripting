#   https://www.geeksforgeeks.org/replace-multiple-lines-from-a-file-using-python/

import fileinput

def approach(filename, old_lines, new_lines):
    res = []
    with fileinput.FileInput(filename, inplace=True, )as file:
        for line in file:
            for old, new in zip(old_lines, new_lines):
                line = line.replace(old, new)
            res.append(line)
            print(line, end='')
    return res
old_lines = ["i am doing good"]
new_lines = ["i am doing very good"]
res = approach('file.txt', old_lines, new_lines)
for line in res:
    print(line, end='')
with open('file.txt', 'w') as file:
    for line in res:
        file.write(line)