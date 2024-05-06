
# Find the chars in a string

def string(n):
    # Solution - 1 
    freq = {}
    for c in set(n):
        freq[c] = n.count(c)
    return freq
    # Solution - 2
    # freq = {}
    # for c in n:
    #     if c not in freq :
    #         freq[c] = 0 
    #     freq[c] +=1
    # return freq


if __name__ == "__main__":
    n = input("Enter the string: ")
    result = string(n)
    print (result)