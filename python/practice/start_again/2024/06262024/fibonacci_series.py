# Write Fibonacci Series 

fib = [0,1]
for i in range(5):
    fib.append(fib[-1] + fib[-2])
print (', '.join(str(e) for e in fib))