#Python Program to Print Multiplication Table
#Write a Python Program to Print Multiplication Table using For Loop and While Loop with an example.
#https://www.tutorialgateway.org/python-program-to-print-multiplication-table/
def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    for i in range (a,b):
        for j in range (1, b+1):
            print ("{} * {} = {}".format(i,j,i*j))
        print ("==================")
    
if __name__ == "__main__":
    main()