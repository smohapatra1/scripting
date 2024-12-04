#   https://www.geeksforgeeks.org/attaching-a-decorator-to-all-functions-within-a-class-in-python/

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

class DecorateAllMethods:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for attr, value in cls.__dict__.items():
            if callable(value):
                setattr(cls, attr, my_decorator(value))

class MyClass(DecorateAllMethods):
    def method1(self):
        print("Executing method1")
    
    def method2(self):
        print("Executing method2")

obj = MyClass()
obj.method1()
obj.method2()