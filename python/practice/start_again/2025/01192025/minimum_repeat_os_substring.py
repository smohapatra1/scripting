#   https://www.geeksforgeeks.org/problems/minimum-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it--170645/1?page=1&category=Pattern%20Searching&sortBy=submissions

#   https://www.geeksforgeeks.org/minimum-number-of-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it/

def MinRepeat(s1, s2):
    n = len(s1)
    m = len(s2)
    x = (m + n - 1) // n
    if s2 in s1 * x:
        return x
    elif s2 in s1 *( x + 1 ):
        return x +1 
    else:
        return -1

if __name__ == "__main__":
    s1 = "ww"
    s2 = "www"
    s3 = "abcd"
    s4 = "cdabcdab" 
    print (MinRepeat(s1, s2))
    print (MinRepeat(s3, s4))