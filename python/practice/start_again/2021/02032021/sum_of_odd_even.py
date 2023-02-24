#Python Program to Calculate Sum of Odd Numbers
#Write a Python Program to Calculate Sum of Odd Numbers from 1 to N using While Loop, and For Loop with an example.
# Sum of even numbers as well 

def main():
    n = int(input("Enter the N numbers you want : "))
    even = 0 
    odd = 0 
    for i in range (1, n+1):
        #EVEN
        if i % 2 == 0 :
            even = even + i 
        else:
            odd = odd + i 
    print ("Sum of ODD = % d AND Sum of Even = %d " % ( odd, even ))

if __name__ == "__main__":
    main()