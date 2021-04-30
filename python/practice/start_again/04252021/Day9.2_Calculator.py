#Design a calculator 

def add (n1, n2):
    return n1 + n2
def sub (n1, n2):
    return n1 - n2
def mul (n1, n2):
    return n1 * n2
def div (n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculator():
    num1=float(input("Enter the first number : "))
    for operators in operations:
        print (operators)
    dead_end=False
    while dead_end == False:
        action=input("Pick the operations from line abobe: ")
        num2=float(input("Enter the 2nd number: "))
        calculation_function=operations[action]
        answers=calculation_function(num1, num2)
        print (f" {num1} {action} {num2} = {answers}")

        ask=input("Enter 'y' to continue or 'n' to exit: ") 
        if ask == "y":
            num1 = answers
        else:
            print ("Exit the calculation ")
            dead_end=True
            calculator()
calculator()
