#Create Fibonanci series 
def fibo(n):
    a = 1
    b = 1 
    for i in range(n):
        yield a
        a,b = b, a+b
for num in fibo(10):
    print ("Using Generator ", num)

#Way2
def fiboo (n):
    output = []
    a = 1 
    b = 1
    for x in range(n):
        output.append(a)
        a,b = b, a+b
    return output
for num in fiboo(10):
    print ("Using Non generator ", num)
