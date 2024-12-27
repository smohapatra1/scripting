#Function Exercise 12 (Calculate Monthly Payment for a Loan)
def emi(p, roi, y):
    r = float(roi/(100*12))
    print ("ROI = %.4f " % r)
    #memi = p * ( r * (( 1 + r) ** (y*12)))/(((1+r)**(y*12)) - 1)
    memi = p * (r*((1.0+r)**(12*y))/(((1.0+r)**(12*y))-1.0))
    print ("Monthly EMI %.3f"  %memi)
emi (10000,20.0, 30)
#emi(input("Enter principal values : ") , input("Enter the Rate of Interest : "), input("Enter the number of years : ") )
