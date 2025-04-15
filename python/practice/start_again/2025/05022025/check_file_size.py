#   https://www.geeksforgeeks.org/how-to-check-file-size-in-python/

from pathlib import Path
f = Path('file2.txt').stat().st_size
print (f)

