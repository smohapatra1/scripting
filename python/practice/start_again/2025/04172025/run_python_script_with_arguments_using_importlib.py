#   https://www.geeksforgeeks.org/how-to-run-another-python-script-with-arguments-in-python/

import importlib.util
arg1 = 'test1'
arg2 = 'test2'
arg3 = 'test3'
spec = importlib.util.spec_from_file_location('test', 'test_script.py')
test = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test)
test.main(arg1, arg2, arg3)