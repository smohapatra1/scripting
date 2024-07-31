#   Check if the Following Number Is an Armstrong Number.

def Armstrong(n):
    t = 0 
    for i in n: 
        t += int(i) ** len(n)
    print (n, "Armstrong") if  t == int(n) else print (n, "Not Armstrong")

if __name__ == "__main__":
    n = input("Enter a number : ")
    result = Armstrong(n)