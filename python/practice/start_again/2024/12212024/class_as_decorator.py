#   https://www.geeksforgeeks.org/class-as-decorator-in-python/

import time
class TimeDecorator:
    def __init__(self, func):
        self.func = func
    def __call__ (self, *args, **kwargs):
        startTime = time.time()
        result = self.func(*args, *kwargs)
        endTime = time.time()
        print (f"Function {self.func.__name__} executed in {endTime - startTime} seconds")
        return result
@TimeDecorator
def exp_func(n):
    total = 0 
    for i in range(n):
        total += i
    return total
print (exp_func(1000000)) 

