#Mortgage Calculator 
#- Calculate the monthly payments of a fixed term mortgage 
#over given Nth terms at a given interest rate. 
#Also figure out how long it will take the user to pay back the loan. 
#For added complexity, add an option for users 
#to select the compounding interval (Monthly, Weekly, Daily, Continually).


#Steps:
# Get the loan amount 
# Get the interest rate 
# Get the Term , Assume 30 years 
# Get Monthly amount = Total % Interest Rate /360

#https://medium.com/towards-artificial-intelligence/mortgage-calculator-python-code-94d976d25a27
import numpy as np
def calculate_emi(loan_amount, Interest_Rate, Term):
    #print ("EMI : %.2f " %((loan_amount * Interest_Rate ) / (Term* 12) ))
    #Different Way
    Loan_Term = Term * 12 
    Rate = 1 + (Interest_Rate/(12* 100))
    Monthly_Payment = loan_amount*(Rate**Loan_Term)*(1 - Rate)/(1-Rate**Loan_Term)
    print ("Montly Payment %.2f" % Monthly_Payment)
    
    Monthly_Interest = []
    Monthly_Balance = []
    for i in range (1, Loan_Term + 1):
        Interest = loan_amount*(Rate-1)
        loan_amount = loan_amount - ( Monthly_Payment - Interest)
        Monthly_Interest = np.append(Monthly_Interest, Interest)
        Monthly_Balance = np.append(Monthly_Balance, loan_amount)
    print ("Balance : ", Monthly_Balance)
    

def main():
    loan_amount = float(input("Enter loan amount: "))
    Interest_Rate = float(input("Enter Interest Rate: "))
    Term = int(input("Enter the term: "))
    calculate_emi(loan_amount, Interest_Rate, Term)
if __name__ == "__main__":
    main()
