#   https://www.geeksforgeeks.org/maximum-length-prefix-one-string-occurs-subsequence-another/

def MaxPrefix(S, T):
    count = 0
    for i in range(0, len(T)):
        if count == len(S):
            break
        if T[i] == S[count]:
            count = count +1
    return count

if __name__ == "__main__":
    S = "digger"
    T = "biggerdiagram"
    S1 = "geeksforgeeks"
    T1 = "agbcedfeitk"
    print (MaxPrefix(S,T))
    print (MaxPrefix(S1,T1))