#   https://www.geeksforgeeks.org/python-program-to-count-the-number-of-blank-spaces-in-a-text-file/

import functools

with open('file.txt') as file:
    file_char = functools.partial(file.read, 1)
    for char in iter(file_char, " "):
        if char == " ":
            count += 1
    print ("count: ", count)