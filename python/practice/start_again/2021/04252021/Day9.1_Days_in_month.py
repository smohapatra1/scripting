#Days in Month
#Instructions
#In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

#You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

#days_in_month(year=2022, month=2)
#And it will use this information to work out the number of days in the month, then return that as the output, e.g.:
#28
#The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.


#Getting leap year
#def leap_year(year):
#    if year % 1 == 0 and year % 400 == 0 and year % 100 != 0:
#        print (f"{year} is a leap year")
#    else:
#        print (f"{year} is not a leap year")
#leap_year(year=int(input("Enter the year: ")))

import time
import calendar
def day_of_month(year, month):
    #Docstring
    """ Test the leap year days """
    if month > 12 or month < 1:
       return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 or year % 100 !=0 and year % 400 == 0 :
        #return True
        Cmonth=month_days[month-1]
        print (f"Current Month Days - {Cmonth}")
        print (calendar.month(year,month))
    else:
        print (f"{year} is not leap year")
day_of_month(year=int(input("Enter the year: ")), month=2)