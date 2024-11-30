#   https://www.geeksforgeeks.org/returning-a-function-from-a-function-python/

def B():
    print ("Inside the method B")
def A():
    print ("Inside the method A")
    return B 
returned_function = A()
returned_function()
