#Write a program that asks the user for a positive number 'n' as input. Assume that the user enters a number greater than or equal to 3 and print a triangle as described below. For example if the user enters 6 then the output should be:
def triag(x):
    my_fun=[]
    for i in range(1,x):
        my_fun.append("*"*i)
    print("\n".join(my_fun))

triag(int(input("Enter a number ")))
