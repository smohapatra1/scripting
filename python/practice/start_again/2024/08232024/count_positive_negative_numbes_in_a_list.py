#   https://www.geeksforgeeks.org/python-program-to-count-positive-and-negative-numbers-in-a-list/

def GetCounts(n):
    pos = 0 
    neg = 0 
    for i in n:
        if i < 0:
            neg += 1
        else:
            pos += 1
    print ("Count of Positive nums = {} and Count of Negative nums = {}".format(pos, neg))

if __name__ == "__main__":
    n = [ -1, 5, -2, -9, 0, 10, 20]
    result = GetCounts(n)