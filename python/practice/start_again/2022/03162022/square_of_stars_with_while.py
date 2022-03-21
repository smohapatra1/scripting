#Draw a square of stars with while 

def square_of_stars_with_while(n):
    i=0
    while i < n:
        stars=" "
        j=0
        while j < n:
            stars+="* "
            j +=1
        print (stars)
        i +=1
square_of_stars_with_while(int(input("Enter the number of stars ")))