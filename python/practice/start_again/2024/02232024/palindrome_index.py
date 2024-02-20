#   https://www.hackerrank.com/test/crlnp8rgs12/questions/a2b68fq8p7b
#   palindromeIndex

def ispalindrome(s):
    for i in range(len(s)//2):
        if s[i] !=s[len(s)-i-1]:
            return False
    return True


def palindromeIndex(s):
    for i in range(len(s)//2):
        j=len(s)-i-1
        if s[i] != s[j]:
            if ispalindrome(s[0:i] + s[i+1:]):
                return i 
            elif ispalindrome(s[0:j] + s[j+1:]):
                return j 
    return -1

if __name__ == "__main__":
    q=int(input().strip())
    for q_itr in range(q):
        s=input()
        result=palindromeIndex(s)
        print (result)

