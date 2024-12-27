#Find LCM
def gcd(x,y):
    if x > y:
        small = x
    else:
        small = y
    for i in range(1, small+1):
        if ( (x% i == 0 ) and (y% i == 0)   ):
            gcd =i
    print ("GCD- ", gcd)
    return gcd

def lcm(x,y):
    lcm = (x* y) //gcd(x,y)
    print ("LCM- ", lcm)


lcm(int(input("x : ")) , int(input("y : ")))
