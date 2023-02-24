#Python Program to Print Natural Numbers
#Write a Python Program to Print Natural Numbers using While Loop and For Loop with an example.

def main():
    a = int(input("Enter a number "))
    for i in range(1,a+1):
        print (i,end=' ')

if __name__ == "__main__":
    main()