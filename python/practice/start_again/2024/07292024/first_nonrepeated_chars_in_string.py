# Print first non-repeated chars in a string 
from collections import Counter

def NonRepeatedChars(t):
    # Solution - 01 
    # ord = []
    # count = {}
    # for c in t:
    #     if c in count :
    #         count [c] +=1
    #     else:
    #         count[c] = 1
    #         ord.append(c)
    # for x in ord:
    #     if count[x] == 1 :
    #         return x
    # return None
    # Solution - 02 
    c = Counter(t)
    for i in t:
        if c[i] == 1:
            return i
    return '_'



if __name__ == "__main__":
    t = input("ENTER THE STRING")
    result = NonRepeatedChars(t)
    print (result)