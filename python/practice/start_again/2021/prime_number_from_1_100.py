#Python Program to print Prime Numbers from 1 to 100
#Write a Python Program to print Prime numbers from 1 to 100, or 1 to n, or minimum to maximum with example. In this Python program, we also calculate the sum of prime numbers from 1 to n.

def main():
    n = int(input("Enter a number: "))
    for num in range (1, n +1):
        count = 0 
        a = []
        for i in range ( 2, num//2 +1 ):
            if num % i == 0:
                count = count + 1
                #a.append(i)
                break
        if count == 0 and num !=1:
            print ("%d " %num, end=' ')

if __name__ == "__main__":
    main()