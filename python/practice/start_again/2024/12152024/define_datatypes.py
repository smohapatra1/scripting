#   https://www.geeksforgeeks.org/explicitly-define-datatype-in-a-python-function/

def add(num1, num2):
    print ("Num1 type is ", type(num1))
    print ("Num2 type is ", type(num2))
    return num1 + num2
    

if __name__ == "__main__":
    print (add(2, 3))
    print (add(float(2), float(3)))