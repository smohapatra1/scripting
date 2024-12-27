#Write a function that normalizes a vector (finds the unit vector). A vector can be normalized by dividing each individual component of the vector by its magnitude. Your input for this function will be a vector i.e. 1 dimensional list containing 3 integers. For example if the input list is:

#vector = [2, 3, -4]
#Then you should return the unit vector(1-Dimensional list) such as:
#[0.3713906763541037, 0.5570860145311556, -0.7427813527082074]
def vector(x,y,z):
    mag = ((x ** 2) + (y ** 2) + (z ** 2) ) ** (1/2)
    a = x/mag
    b = y/mag
    c = z/mag
    print (a, b, c)
vector(2,3,-4)
