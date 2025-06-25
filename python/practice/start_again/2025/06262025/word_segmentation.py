#   https://search.brave.com/search?q=You+are+given+four+words+-+apple%2C+pear%2C+pier%2C+and+pie.+Can+this+be+completely+segmented%3F+If+yes%2C+then+how%3F+using+python&source=web&summary=1&conversation=922a9cfd5f82793c8d1f4b

def word_break(s, word_dict):
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp = True
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]

s = "applepie"
word_dict = ["apple", "pear", "pier", "pie"]
result = word_break(s, word_dict)
print ("Can be segmented: ", result)
