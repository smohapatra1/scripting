#   https://www.geeksforgeeks.org/how-to-count-number-of-instances-of-a-class-in-python/
class X:
    counter = 0 
    def __init__(self):
        X.counter +=1
if __name__ == "__main__":
    g1 = X()
    g2 = X()
    g3 = X()
    print (X.counter)

