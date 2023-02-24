
#FIND 33:
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False
def num(*args):
    for k in args:
        if k[0] == 3 and k[1] == 3 :
            print ("True")
        else:
            print ("False")
num(1,3,3)