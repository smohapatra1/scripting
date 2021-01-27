#Python Program to Print Even Numbers from 1 to N
#Write a Python Program to Print Even Numbers from 1 to N using While Loop and For Loop with an example.

def main():
    a = int(input("Enter a number for the range : "))
    i = 0 
    for num in range (0,a):
        if num % 2 == 0 :
            print ("{}".format(num), end=' ')
    i +=1   
    #way2
    for num in range (2,a+1,2):
        print ("\n {}".format(num), end=' ')


if __name__ == "__main__":
    main()