# Find the middle elements from a list 

def Middle(n):
    mid = int((len(n)/2))
    print (n[mid])

if __name__ == "__main__":
    n = input().rstrip().split()
    res = Middle(n)