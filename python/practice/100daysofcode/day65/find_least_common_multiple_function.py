# Find least common multiple functions
#Write a function that accepts two positive integers as function parameters and returns their least common multiple (LCM). The LCM of two integers a and b is the smallest (non zero) positive integer that is divisible by both a and b. For example, the LCM of 4 and 6 is 12, the LCM of 10 and 5 is 10. 


def lcm(x, y):
    #z = x * y
    #print (z)
    if x > y:
        z = x
    else:
        z = y
    while(True):
        if (( z % x == 0 ) and (z % y == 0)):
            lcm = z
            break
        z +=1

    print ("LCM - ", z)

lcm(int(input("Enter x : ")),int(input("Enter y : ")))


