#   https://www.geeksforgeeks.org/python-program-for-anagram-substring-search-or-search-for-all-permutations/

def search(pat, txt):
    M = len(pat)
    N = len(txt)
    sortedpat = ''.join(sorted(pat))
    res = []
    for i in range(N - 1 +1):
        curr = txt[i:i +M]
        curr = ''.join(sorted(curr))
        if sortedpat == curr:
            res.append(i)
    return res

if __name__ == "__main__":
    txt = "BACDGABCDA"
    pat = "ABCD"
    result = search(pat, txt)
    for idx in result:
        print (f'Text {pat} Indexes are found At {idx}')