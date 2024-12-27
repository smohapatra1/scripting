#!/usr/bin/python
#Write a program which asks the user to enter an integer 'n' which would be the total numbers of hours the user worked in a week and calculates and prints the total amount of money the user made during that week. If the user enters any number less than 0 or greater than 168 (n < 0 or n > 168) then your program should print INVALID 
a = int(input('Enter total number of hours worked in a week: '))
if a <= 0 or a > 168 :
    print ('INVALID')
else:
    #hourly_rate=float(((a/7) / 24))
    #print ( hourly_rate )
    hour = int(a / 7)
    print (hour)
    if hour <= 40 :
        hourly_rate = 8
        #weekly_money = hourly_rate * hour * 7 
        weekly_money = a * hourly_rate 
        print ('YOU MADE %d DOLLARS THIS WEEK' % weekly_money )
    elif hour >=40 or hour <=50:
        hourly_rate = 9
        weekly_money = a * hourly_rate 
        print ('YOU MADE %d DOLLARS THIS WEEK' % weekly_money )
    else:
        hourly_rate = 10
        weekly_money = a * hourly_rate 
        print ('YOU MADE %d DOLLARS THIS WEEK' % weekly_money )


