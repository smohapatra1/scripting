#   https://www.geeksforgeeks.org/python-sympy-matrix-diagonalize-method/

from sympy import * M = Matrix([[1, -3, 3], [3, -5, 3], [6, -6, 4]])  
print("Matrix : {} ".format(M)) 
   
# Use sympy.diagonalize() method  
P, D = M.diagonalize()   
      
print("Diagonal of a matrix : {}".format(D)) 