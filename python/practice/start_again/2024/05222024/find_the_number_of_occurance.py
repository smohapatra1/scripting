#   Find the number of occurrences of a character in a String?

def CharsOccurence(n):
    # d = {}
    # for c in n:
    #     if c not in d:
    #         d[c] = 1
    #     else:
    #         d[c] += 1
    # return d
    d = {}
    for c in set(n):
        d[c] = n.count(c)
    return d

if __name__ == "__main__":
    n = input()
    result = CharsOccurence(n)
    print (result)