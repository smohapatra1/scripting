#   https://www.geeksforgeeks.org/create-a-directory-in-python/

import os 

dir = 'test/test2'

try :
    os.makedirs(dir)
    print (f"Nested dir '{dir}' created successfully")
except FileExistsError:
    print (f"Nested dir '{dir}' exists")
except PermissionError:
    print (f"Nested file '{dir}' creation failed, permission error")
except Exception as e:
    print ("An error occurred '{e}'")

