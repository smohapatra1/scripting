# Define a function with name which_shape.
#The function will ask a number from the user. 
# It will decide the name of the share according to that number and rerun their name
# 3 = Triange
# 4 = Rectangle
# 5 = Pentagon
# 6 = Hexagon
# 7 = and more Polygon 

def which_shape(n):
    if n > 2:
        if n == 3 :
            print (f'Triangle')
        elif n == 4:
            print (f'Rectangle')
        elif n == 5:
            print (f'Pentagon')
        elif n == 6:
            print (f'Hexagon')
        elif n >=7 :
            print ('Polygon')
        else:
            print (f'Polygonnn')

which_shape(int(input("Enter the shape number: ")))
