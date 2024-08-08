# Find the length of the longest word in a given sentence

def longest(s):
    s1 = s.split()
    max_len = max(len(s) for s in s1 )
    return max_len
if __name__ == "__main__":
    s = "I am a good boy"
    result = longest(s)
    print (result)