#Define a function to draw a square of stars


def draw_square(n):
    for i in range(n):
        stars=" "
        for j in range(n):
            stars +="* "
        print (stars)
def while_loop():
    print (f"Using while loop")
    i = 0 
    while i< 4:
        stars=" "
        j=0
        while j <=4:
            stars +="* "
            j +=1
        print (stars)
        i +=1
    
draw_square(int(input("Enter the number of stars: ")))
while_loop()