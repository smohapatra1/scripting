# Type your code here
def lcm(x,y):
    if x > y:
       z = x
    else:
       z = y
    while(True):
        if (( z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z +=1
    print ("LCM - " , z)

lcm(int(input("Enter x: ")), int(input("Enter y: ")))
