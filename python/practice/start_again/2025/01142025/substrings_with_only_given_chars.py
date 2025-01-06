#   https://www.geeksforgeeks.org/count-of-substrings-containing-only-the-given-character/

def CountSubstring(S, C):
    count = 0 
    CCount = 0 
    for ch in S:
        if ch == C:
            CCount +=1
        else:
            count += ((CCount * (CCount +1 ))//2)
            CCount = 0 
    count += ((CCount * (CCount +1))//2)
    print (count)
if __name__ == "__main__":
    S = '0110111'
    C = '1' 
    CountSubstring(S, C)