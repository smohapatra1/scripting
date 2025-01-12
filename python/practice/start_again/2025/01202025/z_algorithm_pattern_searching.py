#   https://www.geeksforgeeks.org/problems/search-pattern-z-algorithm--141631/1?page=1&category=Pattern%20Searching&sortBy=submissions
#   https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/

def getZarr(s, z):
    n = len(s)
    l, r, k = 0, 0, 0 
    for i in range(1, n ):
        if i > r:
            l, r = i, i 
            while r < n and s[r-l] == s[r]:
                r +=1
            z[i] = r -l 
            r -=1 
        else:
            k = i -l 
            if z[k] < r -i +1:
                z[i] = z[k]
            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1

def search(text, pattern):
    concat = pattern + "$" + text
    l = len(concat)
    z = [0] * l 
    getZarr(concat, z)
    for i in range(l):
        if z[i] == len(pattern):
            print ("Pattern Found at index", i-len(pattern)-1)


if __name__ == "__main__":
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    search(text, pattern)
