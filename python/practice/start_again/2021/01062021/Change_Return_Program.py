#Change Return Program - 
#The user enters a cost and then the amount of money given. 
#The program will figure out the change and the number of 
#quarters,dimes, nickels, pennies needed for the change.
#1 quarters = 25 cents 
#1 dime = 10 cents 
#1 nickel = 5 cents 
#1 Pennies = 1 cents 

def main():
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    Money = float(input("Enter the money you gave : "))
    Buy = float(input("Enter the amount you bought : "))
    remaining = Money * 100 - Buy * 100
    QUARTERS = remaining // quarter
    print ("Q ", QUARTERS)
    Qremaining = remaining - QUARTERS * quarter
    #print (Qremaining)
    DIME = Qremaining // dime 
    print ("D ", DIME)
    Dremaining = Qremaining - DIME * dime
    NICKEL = Dremaining // nickel
    print ("N ", NICKEL)
    Nremaining = Dremaining - NICKEL * nickel
    PENNY = Nremaining // penny 
    print ("P ", PENNY)
    Premaining = Nremaining - PENNY * penny 
    print ("Your change : Quart %d , Dime % d , Nickle %d , Penny %d " % (QUARTERS, DIME, NICKEL , PENNY))


if __name__ == "__main__":
    main()