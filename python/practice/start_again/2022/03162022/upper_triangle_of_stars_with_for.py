#Draw a upper triangle of stars with for

def upper_triangle_of_stars_with_for(n):
    for i in range(n,0,-1):
        stars=" "
        for j in range(i):
            stars+="* "
        print (stars)
upper_triangle_of_stars_with_for(int(input("Enter the number of stars ")))