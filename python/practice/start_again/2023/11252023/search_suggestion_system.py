# #   https://leetcode.com/problems/search-suggestions-system/
# 1268. Search Suggestions System
# Medium
# 4.5K
# 222
# Companies
# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

 

# Example 1:

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
# Example 2:

# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Explanation: The only word "havana" will be always suggested while typing the search word.

from typing import List
def searchSuggestion(products : List[str], searchWord: [str]) -> List[List[str]]:
    list_=[]
    products.sort()
    for i, c in enumerate(searchWord):
        products=[ p for p in products if len(p) > i and p[i] == c ]
        list_.append(products[:3])
    return list_



if __name__ == "__main__":
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    print ("{}".format(searchSuggestion(products, searchWord)))

