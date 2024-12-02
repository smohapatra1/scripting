#   https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/

def shout(text):
    return text.upper()
print (shout('Hello'))
yess = shout
print (yess('Hello'))