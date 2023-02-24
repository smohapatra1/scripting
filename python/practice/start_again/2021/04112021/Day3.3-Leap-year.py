## Leap Year

# 💪This is a Difficult Challenge 💪

# Instructions

#Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# The reason why we have leap years is really fascinating, 
# this video does it more justice:
#[https://www.youtube.com/watch?v=xX96xng7sAE]
#(https://www.youtube.com/watch?v=xX96xng7sAE)

#Solution:
#> `on every year that is evenly divisible by 4
#>   **except** every year that is evenly divisible by 100
#>     **unless** the year is also evenly divisible by 400`

year=int(input("Enter the year you want to validate: "))
if year % 4 == 0 or year % 100 != 0 and year % 400 == 0 :
    #print (f"The year {year} is leap")
    print ("Leap year.")
#elif year % 100 == 0 :
#    print (f"The year {year} is leap")
#elif year % 400 == 0 :
#    print (f"The year {year} is leap")
else:
    #print (f"The year {year} is Not leap")
    print ("Not leap year.")