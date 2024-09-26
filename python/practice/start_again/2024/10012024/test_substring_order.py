#   https://www.geeksforgeeks.org/python-test-substring-order/

def test(test_str, K ):
    ns = ""
    for i in test_str:
        if i in K:
            ns += i
    res = False
    if(ns.find(K) != -1):
        res = True
    return res


if __name__ == "__main__":
    test_str = 'geeksforgeeks'
    K = 'seek'
    result = test(test_str, K)
    print (result)