#''Write a function that accepts two numbers a and b as function parameters, 
#and returns True if the sum of the two numbers is an even number, False otherwise.''
def fun1(a,b):
    c = a + b 
    if c % 2 == 0:
        print ("True")
    else:
        print ("False")

fun1(int(input("Enter a: ")),int(input("Enter b:"))) 
