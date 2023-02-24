#Python Program to find GCD of Two Numbers
#Write a Python program to find GCD of two numbers using While Loop, Functions, and Recursion. To find the GCD or HCF in Python, we have to pass at least one non-zero value
#The Greatest Common Divisor (GCD) is also known as Highest Common Factor (HCF), or Greatest Common Factor (GCF), or Highest Common Divisor (HCD), or Greatest Common Measure (GCM).
#In Mathematics, the Greatest Common Divisor (GCD) of two or more integers is the largest positive integer that divides given integer values without the remainder. For example, the GCD value of integer 8 and 12 is 4 because both 8 and 12 are divisible by 1, 2, and 4 (the remainder is 0), and the largest positive integer among them is 4.

def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    i = 1 
    while (i <= n1 and i <= n2) :
        if (n1 % i == 0 or n2 % i == 0) :
            gcd = i
        i = i + 1
    print ("HCD = %d" % gcd)
if __name__ == "__main__":
    main()