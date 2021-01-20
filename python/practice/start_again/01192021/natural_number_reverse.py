#Python Program to Print Natural Numbers in Reverse Order
#Write a Python Program to Print Natural Numbers in Reverse Order with an example.

def main():
    a = int(input("Enter the number: "))
    i = 1
    for i in range(0,a):
        print (a-i, end=' ')
        i +=1

if __name__ == "__main__":
    main()