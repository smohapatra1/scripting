# #   https://leetcode.com/problems/naming-a-company/

# 2306. Naming a Company
# Hard
# 1.9K
# 66
# Companies
# You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

# Choose 2 distinct names from ideas, call them ideaA and ideaB.
# Swap the first letters of ideaA and ideaB with each other.
# If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
# Otherwise, it is not a valid name.
# Return the number of distinct valid names for the company.

 

# Example 1:

# Input: ideas = ["coffee","donuts","time","toffee"]
# Output: 6
# Explanation: The following selections are valid:
# - ("coffee", "donuts"): The company name created is "doffee conuts".
# - ("donuts", "coffee"): The company name created is "conuts doffee".
# - ("donuts", "time"): The company name created is "tonuts dime".
# - ("donuts", "toffee"): The company name created is "tonuts doffee".
# - ("time", "donuts"): The company name created is "dime tonuts".
# - ("toffee", "donuts"): The company name created is "doffee tonuts".
# Therefore, there are a total of 6 distinct company names.

# The following are some examples of invalid selections:
# - ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
# - ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
# - ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
# Example 2:

# Input: ideas = ["lack","back"]
# Output: 0
# Explanation: There are no valid selections. Therefore, 0 is returned.
 
from collections import defaultdict
from typing import List
def naming_company(ideas: List[str]) -> int:
    names=defaultdict(set)
    res=0
    for i in ideas:
        names[i[0]].add(i[1:])
    arr=list(names.keys())
    ans, n=0, len(arr)
    for i in range(n):
        for j in range(i+1, n ):
            a= arr[i]
            b=arr[j]
            res +=len(names[a]-names[b])*len(names[b]-names[a])*2
    return res



if __name__ == "__main__":
    ideas = ["coffee","donuts","time","toffee"]
    print ("{}".format(naming_company(ideas)))