#Calculate the EMI for a loan amount
def _calculate_payment(principle, interest_rate_per_year, duration):
    if interest_rate_per_year==0:
        #return principle/(duration*12)
        print (principle/(duration*12))
    r=interest_rate_per_year/100/12
    n=duration*12
    montly_payment=principle*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
    return montly_payment
_calculate_payment(1000, 4.5, 5)
