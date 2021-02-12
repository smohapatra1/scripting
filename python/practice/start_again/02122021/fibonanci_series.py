#Python Fibonacci Series program
#How to Write Python Fibonacci Series program using While Loop, For Loop, and Recursion?. 
# As per Mathematics, Python Fibonacci Series, or Fibonacci Numbers in Python are the numbers displayed in the following sequence. 
# Fibonacci Series = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 …
# If you observe the above Python Fibonacci series pattern, 
# First Value is 0, Second Value is 1, and the following number is the result of the sum of the previous two numbers. For example, Third value is (0 + 1), Fourth value is (1 + 1) so on and so forth.
import os
def main():
    n = int(input("Enter the numbers you want : "))
    i = []
    a = 1
    b = 1 
    x = 1 
    for x in range(n):
        i.append(a)
        a, b = b , a+b        
    print (i)

if __name__ == "__main__":
    main()