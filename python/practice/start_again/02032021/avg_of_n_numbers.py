#Python Program to find Sum and Average of N Natural Numbers
#Write a Python Program to find Sum and Average of N Natural Numbers using While Loop, For Loop, and Functions with an example.

def main():
    n = int(input("Enter the N natural numbers : "))
    sum = 0 
    avg = 0
    for i in range(1, n+1):
        sum = sum + i 
        i = i + 1
    avg = sum / n 
    print ("Sum = %d and Avg = %.2f" % (sum,avg))
if __name__ == "__main__":
    main()