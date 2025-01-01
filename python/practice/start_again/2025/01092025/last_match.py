#   https://www.geeksforgeeks.org/problems/last-match1928/1

def LastMatch(A,B):
    res = A.rindex(B)
    return res
        
if __name__ == "__main__":
    A = 'abcdefghijklghifghsd'
    B = 'ghi'
    # A = 'abdbccaeab'
    # B = 'abc'
    print (LastMatch(A,B))
