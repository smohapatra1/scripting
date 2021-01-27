#Python Program to Check Leap Year
#Write a Python Program to Check Leap Year 
#or Not by using the If Statement, Nested If Statement, and Elif Statement in Python with example. 
#Logic :-
# 366 days 
# must be divisible by 4
# Century year - ends with 00, 1200,2400, 2500 - If divisible by 400 ( leap year), if not then not a leap year

def leap(year):
    if year % 4 == 0:
        print ("{} is a leap year".format(year))
    elif ( year % 400 == 0 ):
        print ("{} is a leap year".format(year))
    elif ( year % 100 != 0):
        print ("{} is NOT a leap year".format(year))
    else:
        print ("{} is NOT a leap year".format(year))

def main():
    year = int(input("Enter the year: "))
    leap(year)

if __name__ == "__main__":
    main()