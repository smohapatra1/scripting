#Python Program to find Sum of Geometric Progression Series
#Write a Python Program to find the Sum of Geometric Progression Series (G.P. Series) with a practical example.
#G.P Series :  1  4  16  64  256 

def main():
    a = int(input("Enter the first number: "))
    n = int(input("Enter the number of GP series : "))
    r = int(input("Enter the common Ratio: "))
    total = 0 
    value = a 
    #Print the GP series 
    print ("G.P Series : ", end=" ")
    for i in range(n):
        print ("%d " %value, end=" ")
        total = total + value
        value = value * r
    print (i)
    print ("\nSum of G.P series = " , total)
if __name__ == "__main__":
    main()