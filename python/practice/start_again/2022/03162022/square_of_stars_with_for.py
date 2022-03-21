#Draw a square of stars with for

def square_of_stars_with_for(n):
    for i in range(n):
        stars=" "
        for j in range(n):
            stars+="* "
            j +=1
        print (stars)
        i+=1
square_of_stars_with_for(int(input("Enter the number of stars ")))