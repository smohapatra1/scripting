#FIND 33:
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#has_33([1, 3, 3]) -  True
#has_33([1, 3, 1, 3]) -  False
#has_33([3, 1, 3]) - False
def has_33(k):
    for i in range (0, len(k)- 1):
        #Method1
        #if k[i] == 3 and k[i+1] == 3:
        #Method2
        if k[i:i+2] == [3, 3]:
            print ("True")
    return False
    print ("False")
has_33([1, 3, 3])