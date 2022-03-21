#Draw a lower triangle of stars with while 

def lower_triangle_of_stars_with_while(n):
    i=0
    while i < n:
        stars=" "
        j=0
        while j <= i:
            stars+="* "
            j +=1
        print (stars)
        i+=1
lower_triangle_of_stars_with_while(int(input("Enter the number of stars ")))