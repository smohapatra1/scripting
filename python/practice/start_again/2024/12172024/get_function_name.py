#   https://www.geeksforgeeks.org/python-how-to-get-function-name/

def GFG():
    return 'I am in GFG'

print ("The function name is Case - 1 : " + GFG.__name__)
print ("The function name is Case - 2 : " + GFG.__qualname__)
