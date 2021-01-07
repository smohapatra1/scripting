#Find Cost of Tile to Cover W x H Floor 
#- Calculate the total cost of tile it would take to cover 
#a floor plan of width and height, 
#using a cost entered by the user.

#Calculate Area = w * h
# Divide Cost/Area

def calculate(a,h,w):
    print ("Cost : %.2f " %(a * w * h))

def main():
    a = float(input("Enter the cost: "))
    h = float(input("Enter height : "))
    w = float(input("Enter width : "))
    calculate(a,h,w)

if __name__ == "__main__":
    main()