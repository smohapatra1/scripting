#Define a function to print the number of the days in the given month.
#Function name will be number_if_days_in_month.
# It will ask month name from the user.
#Number of days in Gregorian calender:
# January - 31
# Feburay - 28 or 29
# March - 31
# Apr - 30
def number_of_days_in_month(n):
    if n>=27 and n <=31:
        if n == 28 or n == 29:
            print (f'Feburary')
        elif n == 30:
            print (f'Apr')
            print (f'June')
            print (f'Spet')
            print (f'Nov')

        elif n >=30:
            print (f'January')
            print (f'March')
            print (f'May')
            print (f'July')
            print (f'Aug')
            print (f'Oct')
            print (f'Dec')
        else:
            print (f'Out of range')
    else:
        print (f'Please enter values > 27 and < 31')
number_of_days_in_month(int(input("Enter the days of month ")))