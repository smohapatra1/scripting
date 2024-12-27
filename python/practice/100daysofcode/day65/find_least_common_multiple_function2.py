# Find least common multiple functions
#Write a function that accepts two positive integers as function parameters and returns their least common multiple (LCM). The LCM of two integers a and b is the smallest (non zero) positive integer that is divisible by both a and b. For example, the LCM of 4 and 6 is 12, the LCM of 10 and 5 is 10. 

#Solution - find gcd and use that to calculate LCM
#Find GCD
def gcd(x,y):
    if x > y:
        z = y
    else:
        z = x
    for i in range (1, z+1):
        if ( (x % i == 0) and (y % i == 0) ):
            gcd = i
    print ("HCF/GCD -", gcd) 
    return gcd
#Find LCM
def lcm(x,y):
    lcm = int(x*y)//gcd(x,y)
    print ("LCM -", lcm)

lcm(int(input("Enter x: ")), int(input("Enter y: ")))
