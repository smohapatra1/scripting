#Calculator - A simple calculator to do basic operators. 
#Make it a scientific calculator for added complexity.
#1- Add
#2- Substract
#3- Multiply
#4- Division

def add(f,s):
    value = f + s
    print (value)

def sub(f,s):
    if f > s :
        value = f - s
        print (value)
    else:
        value = f - s
        print (value)
def mul(f,s):
    value = f * s
    print (value)
def div (f,s):
    value = f / s
    print (value)
def main():
    f = int(input("Enter first number: "))
    s = int(input("Enter second number: "))
    o = int(input("Enter operation : "))
    if o == 1:
        add(f,s)
    if o == 2:
        sub(f,s)
    if o == 3:
        mul(f,s)
    if o == 4:
        div(f,s)

if __name__ == "__main__":
    main()