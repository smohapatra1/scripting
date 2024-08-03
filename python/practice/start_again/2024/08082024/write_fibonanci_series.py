#   Writing Fibonacci Series

def Fibo(fib):
    for i in range(5):
        fib.append(fib[-1] + fib[-2])
    print (', '.join(str(e) for e in fib))

if __name__ == "__main__":
    fib = [ 0, 1]
    result = Fibo(fib)