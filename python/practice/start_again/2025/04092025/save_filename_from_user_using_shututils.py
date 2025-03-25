#   https://www.geeksforgeeks.org/how-to-save-file-with-file-name-from-user-using-python/

import shutil

src = input("Enter src filename :")
dst = input("Enter dst filename :")
shutil.copyfile(src, dst)