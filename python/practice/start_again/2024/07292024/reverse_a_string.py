# Reverse a String

def reverse(t):
    return t[::-1]

if __name__ == "__main__":
    t = input("Enter a string :")
    result = reverse(t)
    print (result)