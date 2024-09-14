#   https://www.geeksforgeeks.org/python-remove-k-length-duplicates-from-string/

def Duplicate(test_str, K ):
    mem = set()
    res = []
    for idx in range(0, len(test_str) -K ):
        sub = test_str[idx: idx +K]
        if sub not in mem:
            mem.add(sub)
            res.append(sub)
    res = ''.join(res[ele] for ele in range(0, len(res), K ))
    return res


if __name__ == "__main__":
    test_str = 'geeksforfreeksfo'
    K = 3
    result = Duplicate(test_str, K )
    print (result)