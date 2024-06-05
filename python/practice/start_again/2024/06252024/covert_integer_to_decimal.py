# Covert an Integer to Decimal

import decimal

def IntToDecimal(n):
    print (decimal.Decimal(n))
    print (type(decimal.Decimal(n)))

if __name__ == "__main__":
    n=int(input())
    result=IntToDecimal(n)