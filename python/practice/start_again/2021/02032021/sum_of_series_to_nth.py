#Python Program to calculate Sum of Series 1²+2²+3²+….+n²
#Write a Python Program to calculate Sum of Series 1²+2²+3²+….+n² using For Loop and Functions with an example.

def main():
    n = int(input("Enter the number of series you want : "))
    total = 0 
    total = n * (n +1 ) * (2 * n + 1)/6
    print ( "Sum = ", total)
if __name__ == "__main__":
    main()