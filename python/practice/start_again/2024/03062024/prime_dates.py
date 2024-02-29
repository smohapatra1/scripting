# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-prime-date/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two

# In this challenge, the task is to debug the existing code to successfully execute all provided test files.

# Given two dates each in the format dd-mm-yyyy, you have to find the number of lucky dates between them (inclusive). To see if a date is lucky,

# Firstly, sequentially concatinate the date, month and year, into a new integer  erasing the leading zeroes.
# Now if  is divisible by either  or , then we call the date a lucky date.
# For example, let's take the date "02-08-2024". After concatinating the day, month and year, we get  = 2082024. As  is divisible by  so the date "02-08-2024" is called a lucky date.

# Debug the given function findPrimeDates and/or other lines of code, to find the correct lucky dates from the given input.

# Note: You can modify at most five lines in the given code and you cannot add or remove lines to the code.

# To restore the original code, click on the icon to the right of the language selector.

# Input Format

# The only line of the input contains two strings  and  denoting the two dates following the format dd-mm-yyyy. Consider,  is the day number,  is the month number and  is the year number.

# Note: Here  means January,  means February,  means March and so on and all the dates follow the standard structure of English calender including the leap year.

# Constraints




# Output Format

# For each test cases, print a single integer the number of lucky dates between  and  in a single line.


import re
month = []

def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 29 # Change 1
    elif year % 100 == 0:
        month[2] = 28
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28

def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31

def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while(True):
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1 # Change2
        if x % 4 == 0 or x % 7 == 0: # Change3
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 =  y1 + 1
                m1 = 1 # Change4
    return result;

for i in range(1, 15):
    month.append(31)

line = input()
date = re.split('-| ', line)
d1 = int(date[0])
m1 = int(date[1])
y1 = int(date[2])
d2 = int(date[3])
m2 = int(date[4])
y2 = int(date[5])

result = findPrimeDates(d1, m1, y1, d2, m2, y2)
print(result)



