#   https://www.geeksforgeeks.org/python-program-check-validity-password/

import re

def ValidatePassword(password):
    flap = 0
    while True:
        if len(password) <= 8:
            flap = -1 
            break
        elif not re.search("[a-z]", password):
            flap = -1 
            break
        elif not re.search("[A-Z]", password):
            flap = -1
            break
        elif not re.search("[0-9]", password):
            flap = -1
            break
        elif not re.search("[_@$]", password):
            flap = -1
            break
        elif re.search("\s", password):
            flap = -1 
            break
        else:
            flap = 0 
            print ("Valid Password")
            break
    if flap == -1:
        print ("Invalid Password")

if __name__ == "__main__":
    s = "R@m@_f0rtu9e$"
    ValidatePassword(s)