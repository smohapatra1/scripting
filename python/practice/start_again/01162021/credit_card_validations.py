#Credit Card Validator - 
#Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) 
#and validates it to make sure that it is a valid number (look into how credit cards use a checksum).

#Thought
#Check the card type
#Check the number of digits - must be 16 digits 
#Check the name on card 
# Check the year of expiry - make sure it is > current date 

from datetime import date
from datetime import datetime
def check_valid_card(cNumber,eYear, eMonth):
    get_len=len(cNumber)
    if get_len < 16 :
        print ("Please enter a valid card, must be 16 digits ")
    else:
        validate_card_expiry(eYear, eMonth)

def validate_card_expiry(eYear, eMonth):
    #Validate the expiry date
    #print (date.today())
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    print ("%s and %s " % (now, dt_string))
    #Get month
    month = now.strftime("%m")
    year = now.strftime("%Y")
    print ("Current Month and Year : %s:%s" %(month,year))
    if eYear < year :
        print ("Card is expired, use a valid card ")
    elif (eMonth == month or eYear == year ):
        print ("Card is Valid")
    elif (eMonth <= month and eYear == year ):
        print ("Card is expired, use valid card ")
    else:
        print ("Card is valid") 




def main():
    cNumber=input("Enter the number: ")
    eYear = str(input("Enter Expired year  YYYY: "))
    eMonth = str(input("Enter Expired month m: ")) 
    check_valid_card(cNumber,eYear, eMonth)

if __name__ == "__main__":
    main()