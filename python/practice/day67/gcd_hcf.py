#GCD and HCF problem

def gcd(x,y):
    if x >y:
        small = x
    else:
        small = y
    for i in range(1, small+1):
        if ( (x % i == 0) and (y % i == 0) ):
            lcm = i 
    print ("GCD " , lcm)

gcd(4,6)

