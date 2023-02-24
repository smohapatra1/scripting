#Validate credit card using modulous-10 algorithm
#https://www.codeproject.com/Tips/515367/Validate-credit-card-number-with-Mod-10-algorithm
#Card Length 

#Typically, credit card numbers are all numeric and the length of the credit card number is between 12 digits to 19 digits. 

#14, 15, 16 digits – Diners Club
#15 digits – American Express
#13, 16 digits – Visa
#16 digits - MasterCard  

# This is incomplete 


def validate_card():
    cNumber = input("Please enter the card number : ")
#get the lenth of number     
    get_len = len(cNumber)
    print ("Lenth of card number: ", get_len)

#Break the number into list 
    place = list(cNumber)

#using slice notation get the even and odd places from list 
    even_places = place[1::2]
    print ("Even places : ", even_places)
    odd_places = place[0::2]
    print ("Odd places : ", odd_places)
# Now multiply 2 in each of numbers in even place 
#Step 1 - Starting with the check digit double the value of every other digit (right to left every 2nd digit) 

    sq_num = [num ** 2 for num in str(even_places)]
    print (sq_num)

#If doubling of a number results in a two digits number, 
#add up the digits to get a single digit number. This will results in eight single digit numbers.


#Now add the un-doubled digits to the odd places

# Add up all the digits in this number 


def main ():
    validate_card()
    

if __name__ == "__main__":
    main()