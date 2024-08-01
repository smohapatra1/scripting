#   Write a Python program to check if a number is prime.

def Prime(n):
    if n % 2 == 0:
        print ("{} is Prime".format(n))
    else:
        print ("{} is NOT Prime".format(n))

if __name__ == "__main__":
    n = int(input("Enter a number"))
    result = Prime(n)