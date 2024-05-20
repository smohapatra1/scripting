# How do you reverse an array?

def Reverse(a):
    b = (a[::-1])
    return b 

if __name__ == "__main__":
    #a = int(input().strip().split())
    a = [int (i) for i in input().strip().split()]
    result = Reverse(a)
    print (result)