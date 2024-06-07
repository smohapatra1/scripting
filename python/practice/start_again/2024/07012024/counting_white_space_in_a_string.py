# Counting white spaces in a string

def WhiteSpace(n):
    a = len(n)
    count = 0 
    for i in n:
        if i == ' ':
            count +=1
    print (count)


if __name__ == "__main__":
    n = input().rstrip()
    res = WhiteSpace(n)