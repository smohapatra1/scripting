#A function will ask the user to enter an integer between 1 and 7. 
# It will decide the name according to that number
def day_of_week(n):
    if n <= 7 and n >= 0:  
        if n == 1:
            print (f'Monday')
        elif n ==2 :
            print (f'Tuesday')
        elif n == 3 :
            print (f'Wednesday')
        elif n == 4 :
            print (f'Thursday')
        elif n == 5 :
            print (f'Friday')
        elif n == 6:
            print (f'Saturday')
        elif n == 7 :
            print (f'Sunday')
    else:
        print ('Please enter the number between 1 and 7 ')
day_of_week(int(input("Please enter a numebr betwen (1-7) : ")))
    
