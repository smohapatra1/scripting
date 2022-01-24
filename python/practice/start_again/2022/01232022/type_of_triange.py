#Define a function to ask the length of sides of a triangle.
#Function name is name_the_triange
# The function will decide the type of triange according to the length of the sides
# Types of the trianges:
#  Equilateral: three equal sides
#  Isosceles : two equal sides
#  Scalene :- No equal sides

def name_the_triange(a,b,c):
    if a == b == c :
        print (f'Equilatereal')
    elif a != b != c:
        print (f'Scalene')
    elif a == b or b == c or c == a :
        print (f'Isosceles')
    else:
        print (f' Does\'t match' )
name_the_triange(int(input("Enter the First Side : ")), int(input("Enter the Seond Side : ")), int(input("Enter the thirst side : ")))
