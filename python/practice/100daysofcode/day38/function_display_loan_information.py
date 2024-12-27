#Display loan information
#Write a program for loan calculations. Your program should ask the user for three pieces of information (with three seperate input() functions:)
#Total amount of loan.
#Annual interest rate. (Assume that the interest rate is a positive integer. For example 5 means that annual interest is 5% (five percent) per year.
#Total duration of loan in years.

#emi
def p_amount(p, i, y):
    roi= float(i/(12*100))
    print ("LOAN AMOUNT  : %d  INTEREST RATE : %.3f " %(p, roi))
    n= y*12
    print ("DURATION (YEARS) : %d NUMBER OF MONTHS : %d " %(y, n))
    #emi
    a = p * ( (roi*(1+roi)**n)/(((1+roi)**n)-1))
    print ("emi : %.3f" %a)

#balance

def bal(p, i, y, pm):
    roi = float(i /12 * 100 )
    n = y * 12
    b = p * ( (((1+roi)**n) - (( 1 +roi) **pm))/(((1+roi)**n) -1 ))

#p_amount ( 10000,20.0, 30)
p_amount ( input("Enter p value ") ,input("Enter interest value " ), input("Enter years "))
#bal ( input("Enter p value ") ,input("Enter interest value " ), input("Enter years "), input("Number of payments made : "))

# Calculation
# Your main program goes here
p=float(input("Enter loan amount: "))
i=float(input("Enter annual interest rate (percent): "))
y=int(input("Enter loan duration in years: "))
#print ("LOAN AMOUNT  : %d  INTEREST RATE : %.3f " %(p, roi))
#print ("DURATION (YEARS) : %d NUMBER OF MONTHS : %d " %(y, n))
a=p_amount(p, i, y)

for yr in range(0,y):
    n = 12 * y
    #print ("aaaaaaaaaaaaaaaa %d" %a) 
    #b = bal ( input("Enter p value ") ,input("Enter interest value " ), input("Enter years "), 12 * y )
    b = bal ( p ,i, y, n )
    #b = p * ( (((1+roi)**n) - (( 1 +roi) **pm))/(((1+roi)**n) -1 ))
    yr +=1
    m = ( float(a) * int(y) * 12)
    #p = b
    print ("year : %d and  balance : %.3f Monthly %s " %(yr,b,m))
