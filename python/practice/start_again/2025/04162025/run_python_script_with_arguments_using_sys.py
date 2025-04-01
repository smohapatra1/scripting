#   https://www.geeksforgeeks.org/how-to-run-another-python-script-with-arguments-in-python/

import sys
arg1 = sys.arg[1]
arg2 = sys.arg[2]
arg3 = sys.arg[3]
print (f' Arguments passed : {arg1}, {arg2}, {arg3}')