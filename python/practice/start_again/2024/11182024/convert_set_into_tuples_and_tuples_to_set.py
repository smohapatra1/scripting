#   https://www.geeksforgeeks.org/python-program-to-convert-set-into-tuple-and-tuple-into-set/

s = {'a', 'b', 'c', 'd', 'e'}
t = ('d', 'b', 'a', 'e', 'c') 
x = [ i for a, i in enumerate(s)]
y = [i for a, i in enumerate(t)]
print ("Converting Sets to Tuple : ", tuple(x))
print ("Converting Tuples to Set : ", set(y))