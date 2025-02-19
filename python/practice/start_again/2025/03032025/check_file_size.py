#   https://www.geeksforgeeks.org/how-to-check-file-size-in-python/

from pathlib import Path
print (Path('file.txt').stat().st_size)