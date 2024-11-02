#   https://www.geeksforgeeks.org/count-of-distinct-substrings-of-a-given-string-using-rabin-karp-algorithm/?ref=leftbar-rightbar

def Main(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substrings.add(s[i:j + 1])
    return len(substrings)

if __name__ == "__main__":
    s = "abcd"
    print ("Results after counting : ", Main(s))