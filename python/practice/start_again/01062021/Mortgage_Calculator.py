#Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage 
#over given Nth terms at a given interest rate. 
#Also figure out how long it will take the user to pay back the loan. 
#For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).


def main():
    loan=float(input("Enter the loan amount: "))
    IR=float(input("Enter the interest rate: "))
    MI = IR / 12 / 100
    Term=float(input("Enter the term of the loan : "))
    months = Term * 12 
    MP = loan * ((MI * (1+MI)**months))/((1 + MI)**(months - 1))

    print ("MI = %.2f : MP = %.2f " %(MI,MP))

if __name__ == "__main__":
    main()