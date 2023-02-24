#Fibonanci series 
def fibo(n):
    output = []
    a = 1
    b = 1

    for num in range (n):
        output.append(a)
        a,b = b , a + b
    return output

if __name__ == "__main__":
    for num1 in fibo(10):
        print (num1)
    