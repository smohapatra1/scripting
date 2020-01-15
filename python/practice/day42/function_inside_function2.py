#''Write a function that accepts two numbers a and b as function parameters, 
#and returns True if the sum of the two numbers is an even number, False otherwise.'' - Using two functions
def fun1(a,b):
    c = a+b
    def addition(c):
        if c % 2 == 0:
            print ("True")
        else:
            print ("False")
    my_result = addition(c)
    return my_result

fun1(int(input("Enter a: ")),int(input("Enter b:"))) 
