#Python Program to find Sum of Arithmetic Progression Series
#Write a Python Program to find the Sum of Arithmetic Progression Series (A.P. Series) with a practical example.
#Arithmetic Series is a sequence of terms in which the next item obtained by adding a common difference to the previous item. 
# Or A.P. series is a series of numbers in which the difference of any two consecutive numbers is always the same. 
# This difference called a common difference.

#In Mathematical behind calculating Arithmetic Progression Series
#Sum of A.P. Series : Sn = n/2(2a + (n – 1) d)
#Tn term of A.P. Series: Tn = a + (n – 1) d

def main():
    a = int(input("Enter the first number: "))
    n = int(input("Enter the how many numbers you want: "))
    d = int(input("Enter the difference : "))
    total = (n * (2 * a + (n-1) * d) /2)
    tn = a + (n-1)* d
    i = a
    print ("A.P series : " , end=" ")
    while ( i <= tn):
        if i != tn:
            print ("%d" %i , end=" ")
        else:
            print ( "%d = %d " %(i, total))
        i = i + d
    print ("\n")

if __name__ == "__main__":
    main()