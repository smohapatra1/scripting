#   https://www.geeksforgeeks.org/problems/cat-and-hat-python/1

def FindStr(str, s1, s2):
    # s = str.lower()
    # # s = str.split(" ")
    # print (s)
    # res = 0 
    # for i in range(0, len(s)):
    #     if ( s1 == s[i]) or ( s2 == s[i] ):
    #         res = res + 1
    #         # return True
    #     # else:
    #     #     return False
    # return res
    number_cat = str.count('cat')
    number_hat = str.count('hat')
    
    return number_cat == number_hat

if __name__ == "__main__":
    str = 'catinahat'
    s1 = "cat"
    s2 = "hat"
    print (s1 + " and " + s2 + " are present in  the " + str + " : ", FindStr(str, s1, s2) )
