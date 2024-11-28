#   https://www.geeksforgeeks.org/matrix-manipulation-python/

import numpy
# initializing matrices 
x = numpy.array([[1, 2], [4, 5]]) 
y = numpy.array([[7, 8], [9, 10]])
print ("Values After adding the elements           : \n", numpy.add(x, y))
print ("Values After Substracting the elements     : \n", numpy.subtract(x, y))
print ("Values After Multiply the elements         : \n", numpy.multiply(x, y))
print ("Values After Divide the elements           : \n", numpy.divide(x, y))