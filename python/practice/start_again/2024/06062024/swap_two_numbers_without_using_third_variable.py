#   How would you swap two numbers without using a third variable?

def Swap(a,b):
    # Tsum = a + b
    # c = Tsum - b 
    # d = c - Tsum
    # return c, d 
    a, b = b, a 
    return a, b 

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    result = Swap(a,b)
    print (result)

