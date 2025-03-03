#   https://www.geeksforgeeks.org/create-a-directory-in-python/

import os 

dir = 'test'
try: 
    os.mkdir(dir)
    print (f"Directory '{dir}' created successfully")
except FileExistsError:
    print (f"Directory '{dir}' already existed")
except PermissionError:
    print (f"Permission denied, unable to create '{dir}'")
except Exception as e:
    print ("An error occurred '{e}'")
