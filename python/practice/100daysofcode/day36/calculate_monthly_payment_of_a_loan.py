#Function Exercise 12 (Calculate Monthly Payment for a Loan) - Incomplete
def emi(x):
    if x >=0 :
        duration = 5
        roi = 4.5
        month=x/(5* 12)
        #Monthky Intereset
        mi = float(month + (x/roi))
        print ("Monthly Int %d" %mi)
        #Number of payments
        np= duration * 12
        mp = float(x/np)
        print ("Monthly Payment  %d" %mp)

    else:
        print("Enter a valid loan amount")

emi(int(input("Enter the laon amount : ")))
