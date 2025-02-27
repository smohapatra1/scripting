#   https://www.geeksforgeeks.org/get-parent-of-current-directory-using-python/

from pathlib import Path
d = Path('c/dos').resolve().parents[0]
print (d)