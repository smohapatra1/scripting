
#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False
def makes_twenty(a,b):
    c = a+b
    print ("Sum = {}".format(c))
    if c != 20:
        print ("False")
    else:
        print ("True")
makes_twenty(10,0)

#2nd way
def twenty(a,b):
    print (a,b)
    return (a+b) == 20 or a==20 or b==20
twenty(20,20) 