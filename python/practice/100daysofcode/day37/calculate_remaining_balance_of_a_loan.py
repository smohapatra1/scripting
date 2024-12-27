#Functions Exercise 13 (Calculate the remaining balance of a loan)
#(principal, annual_interest_rate, duration , number_of_payments)
def bal(p, ri, yr , np):
    r = float(ri/(12*100))
    n_mnths = yr * 12 
    print ("roi % .3f" % r)
    rem_bal = p *(( (( 1 + r ) ** n_mnths ) - ((1 + r ) ** np ))/((( 1+r) ** n_mnths ) -1))  
    print ("rem_balan %.3f" %rem_bal)
bal( 1000, 4.5, 5, 12)
