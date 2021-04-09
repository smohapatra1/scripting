def outer(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b)
result = outer(5,10)
print (result)