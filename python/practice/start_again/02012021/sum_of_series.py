#Python Program to calculate Sum of Series 1³+2³+3³+….+n³
#Write a Python Program to calculate Sum of Series 1³+2³+3³+….+n³ using For Loop and Functions with an example.
#The Mathematical formula for Python Sum of series 1³+2³+3³+….+n³ = ( n * (n+1) / 2)²
import math 
def main():
    n = int(input("Enter the series number you want: "))
    sum = math.pow((n * (n+1))/2,  2)
    print ("sum = ", sum)

    #for i in range(1, n):
    #    print ("{} - >  {} ".format(i,i*i*i) ) 
    #sum = total

if __name__ == "__main__":
    main()