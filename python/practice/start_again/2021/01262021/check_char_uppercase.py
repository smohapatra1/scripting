#Python Program to check character is Lowercase or not
#Write a Python program to check character is Lowercase or not with a practical example.
import os
def main():
    a = str(input("Enter your name: "))
    if (a.islower()):
        print ("{} is in lower case".format(a))
    else:
        print ("{} is NOT in lower case".format(a))

if __name__ == "__main__":
    main()