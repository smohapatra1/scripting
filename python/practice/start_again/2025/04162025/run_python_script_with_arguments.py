#   https://www.geeksforgeeks.org/how-to-run-another-python-script-with-arguments-in-python/

import subprocess
arg1 = 'Test1'
arg2 = 'Test2'
arg3 = 'Test3'
subprocess.run(['python', 'test.py', arg1, arg2, arg3])