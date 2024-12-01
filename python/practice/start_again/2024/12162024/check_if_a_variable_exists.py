#   https://www.geeksforgeeks.org/how-to-check-if-a-python-variable-exists/

var1 = 2

def Variable():
    var = '1'
    if 'var' in locals():
        return True
    elif 'var1' in globals():
        return True
    else:
        return False

print (Variable())