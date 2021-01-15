#Unit Converter (temp, currency, volume, mass and more) 
#Converts various units between one another. 
#The user enters the type of unit being entered, 
#the type of unit they want to convert to and then the value. 
#The program will then make the conversion.

def converter_temp(temp):
    print ("Temprature in degree Centigrade ", temp)
    #Convert to Fahreinheat
    F = (temp * 9/5) + 32
    print ("%.2f degree celcious in Fahrenheit %.2f" %(temp,F))
    # Convert from Fahrenheit to Kelvin
    K = F - 32 * 9/5 + 273.15
    print ("%.2f F in Kelvin %.2f" %(F,K))
    #F - > C
    C = (F - 32) * 5/9
    print ("%.2f Fahrenheit to Celsious %.2f" %(F, C) )
def converter_currency(currency):
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    total = currency * 100
    quarters = total // quarter 
    tdimes = total - quarters * dime
    dimes = tdimes // dime
    #print ("Total Dimes %.2f" % dimes )

    tnickels = total - dimes * nickel
    nickels = tnickels // nickel

    print ("Total Quarters %.2f, Dimes %.2f, Nickels %.2f" %( quarters, dimes, nickel) )
def main():
    temp= float(input("Enter the temparature in degree centigrade: "))
    converter_temp(temp)
    currency = float(input("Enter the currency : "))
    converter_currency(currency)

if __name__ == "__main__":
    main()