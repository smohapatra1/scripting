#   https://www.geeksforgeeks.org/python-loop-through-files-of-certain-extensions/

from pathlib import Path

dir = 'test'
paths = Path(dir).glob('**/*.txt')
for path in paths:
    print (path)
