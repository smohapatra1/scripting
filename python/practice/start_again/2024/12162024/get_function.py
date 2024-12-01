#   https://www.geeksforgeeks.org/python-get-function-signature/

from inspect import signature
def gfg(x: str, y:int):
    pass
t = signature(gfg)
print (t)
print (t.parameters['x'])
print (t.parameters['y'].annotation)