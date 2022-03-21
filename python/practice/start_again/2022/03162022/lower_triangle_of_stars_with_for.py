#Draw a lower triangle of stars with for

def lower_triangle_of_stars_with_for(n):
    for i in range(n):
        stars=" "
        for j in range(i+1):
            stars+="* "
        print (stars)  
lower_triangle_of_stars_with_for(int(input("Enter the number of stars ")))