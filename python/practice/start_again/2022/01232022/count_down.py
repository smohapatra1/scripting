#Define a function mamed count_dowm
# It will ask tow integers from the user 
# Decide which one is small and which one is large
# Then it will print the numbers starting from the large one up to the small one (backwards)
def count_down(a,b):
    small = 0 
    large = 0 
    if a <= b  :
        small = a 
        large = b
        print (f'{b} is large and {a} is small ')
    else:
        small = b
        large = a
        print (f'{b} is small and {a} is large')
    #Call Recurssion
    print_down(small, large)

#Recurrsive Function
def print_down(end, value):
    if value == end:
        print (value)
        return
    else:
        print (value)
        print_down(end, value-1)

count_down(int(input("Enter the First number : ")), int(input("Enter the second number: "))) 
    