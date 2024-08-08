#   Calculate the power of a number.

def power(n, m ):
    return n ** m 

if __name__ == "__main__":
    n = float(input("Enter the base : "))
    m = float(input("Enter the exponent: "))
    result = power(n,m)
    print (result)