#Python Program to find Prime Number
#Write a Python Program to Find Prime Number using For Loop, While Loop, and Functions. Any natural number that is not divisible by any other number except 1 and itself called Prime Number in Python.

def main():
    n = int(input("Enter a number: "))
    i = 2
    count = 0  
    while i < n :
        if n % i == 0 :
            count = count +1
            break
        i = i + 1 
    if count == 0 and n !=0 :
        print ("%d is Prime" % n) 
    else:
        print ("%d is Not Prime" % n)
if __name__ == "__main__":
    main()