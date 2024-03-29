
# #   https://leetcode.com/problems/encode-and-decode-tinyurl/


# 535. Encode and Decode TinyURL
# Medium
# 1.9K
# 3.7K
# Companies
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Implement the Solution class:

# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
 

# Example 1:

# Input: url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"

# Explanation:
# Solution obj = new Solution();
# string tiny = obj.encode(url); // returns the encoded tiny url.
# string ans = obj.decode(tiny); // returns the original url after decoding it.

import hashlib

def __init__(self):
     self.urls ={}

def hash_to(self, s):
     return 'https://tin.e' + hashlib.md5(s.encode()).hexdigest()
def encode(longUrl: str) -> str:
     hash_key=self.hash_to(longUrl)
     self.urls[hash_key] = longUrl
     return hash_key
     
     
def decode(shortUrl : str) -> str:
     return self.urls[shortUrl]

if __name__ == "__main__":
     longUrl = "https://leetcode.com/problems/design-tinyurl"
     sortUrl="http://tinyurl.com/4e9iAk"
     print ("{}".format(encode(longUrl)))
     print ("{}".format(decode(sortUrl)))