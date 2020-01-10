#/usr/bin/python
#Functions Exercise 14 (Display loan information)

def emi(p,i,y):
    if i==0:
        return p/(y*12)
    r = (i/100)/12
    n = y * 12 
    a = p * ( r * ((1.0+r)**n) / ((1.0+r)**n - 1 )  )
    return a
    #print ("emi %.3f " %a)
def bal (p,i,y,np):
    r = (i/100)/12.0
    n = y * 12
    b = p*( ((1.0+r)**n - (1.0+r)**np)/((1.0+r)**n - 1) )
    return b
    #print ("balance %.3f" %b)

p = input("Enter the loan amount : ")
i = input("Enter the intereset rate : ")
y = input("Enter the number of year : ")
a=emi(p,i,y)
print('LOAN AMOUNT:',int(p),'INTEREST RATE (PERCENT):', int(r))
print('DURATION (YEARS):',y,'MONTHLY PAYMENT:',int(a))
#Number of payments
n = y * 12
for yr in (0, y):
    d = bal(p,i,y,yr*12)
    y+=1
    print('YEAR:', yr, 'BALANCE:', d, 'TOTAL PAYMENT', int(a*yr*12))

