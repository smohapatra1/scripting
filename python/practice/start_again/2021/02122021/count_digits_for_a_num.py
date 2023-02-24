#Python Program to Count Number of Digits in a Number
#Write a Python Program to Count Number of Digits in a Number using While Loop, Functions, and Recursion

def main():
    n = int(input("Enter a number : "))
    count = 0 
    while n > 0:
        n = n // 10
        count = count + 1
    print ("The number of digits are %d in %d  " %(count, n))
if __name__ == "__main__":
    main()