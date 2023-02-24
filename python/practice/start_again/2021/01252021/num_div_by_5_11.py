#Python Program to Check Number is Divisible by 5 and 11
#Write a Python program to Check Number is Divisible by 5 and 11 using If Else with an example.

def main():
    a = int(input("Enter a number : "))
    if a % 5 == 0 and a % 11 == 0:
        print ("%d is divisible by 5 and 11" %(a))
    else:
        print ("%d is NOT divisible by 5 and 11" %(a))
if __name__ == "__main__":
    main()