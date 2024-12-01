#   https://www.geeksforgeeks.org/python-program-to-convert-any-base-to-decimal-by-using-int-method/

def AnyNumBase(number, base):
    t = int(number, base)
    return t

if __name__ == "__main__":
    # number = '1011'
    # base = 2
    number = '1A'
    base = 16
    print (" Any number to base : ", AnyNumBase(number, base))