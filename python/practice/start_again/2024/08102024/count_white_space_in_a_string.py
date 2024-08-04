#   Counting the White Spaces in a String

def CountWhite(n):
    # Solution 1 
    count = 0 
    for i in n:
        if i == ' ':
            count += 1
    return count
    # Solution 2
    # print (n.count(' '))

if __name__ == "__main__":
    n = "I am Samar and I am GOOD"
    result = CountWhite(n)
    print (result)