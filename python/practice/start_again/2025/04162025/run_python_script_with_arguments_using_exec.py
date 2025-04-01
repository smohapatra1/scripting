#   https://www.geeksforgeeks.org/how-to-run-another-python-script-with-arguments-in-python/

arg1 = 'test1'
arg2 = 'test2'
arg3 = 'test3'
exec(open('test_script.py').read(), {'arg1': arg1, 'arg2': arg2, 'arg3': arg3})