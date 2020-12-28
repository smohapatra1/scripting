#Fibonacci Sequence - 
#Enter a number and 
#have the program generate the Fibonacci sequence to that number 
#or to the Nth number.
#First print fibonancci series 

def fibo(n):
    i = []
    a = 1
    b = 1 
    for x in range(n):
        i.append(a)
        a,b = b, a+b
    print (i)
    return(i)
def main():
    n = int(input("Enter the number "))
    fibo(n)

if __name__ == '__main__':
    main()