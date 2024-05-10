# Reverse a String


def reverseString(n):
    a = n.lower()
    return a[::-1]


if __name__ == "__main__":
    n = input()
    result = reverseString(n)
    print (result)