#   https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/

def search(pat, txt):
    M = len(pat)
    N = len(txt)
    sortedpat = ''.join(sorted(pat))
    res = []
    for i in range(N - M +1):
        curr = txt[i:i + M ]
        curr = ''.join(sorted(curr))
        if sortedpat == curr:
            res.append(i)
    return res

if __name__ == "__main__":
    txt = "BACDGABCDA"
    pat = "ABCD"
    result = search(pat, txt)
    for idx in result:
        print (idx, end=' ')