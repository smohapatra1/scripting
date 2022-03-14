#Enter a value using fucnction
# It should return some string 
def is_integer(n):
    print (type(n))
    if n.isdigit():
        print(f'The name you entered is/are {n}')
    else:
        print (f'Please enter the input as String')
is_integer(input("Enter a number: "))