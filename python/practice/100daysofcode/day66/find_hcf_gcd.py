#Find the highest common factor or GCD - greatest common divisior
def hcf(x,y):
    if x > y:
        small = x
    else:
        small = y
    for i in range (1, small+1):
        if ( (x % i == 0) and (y % i == 0)):
            hcf = i
    #return hcf
    print ("HCF/GCD - ", hcf)

hcf(int(input("Enter x: ")), int(input("Enter y: ")))
