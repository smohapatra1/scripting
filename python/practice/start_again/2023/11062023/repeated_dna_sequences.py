# #   https://leetcode.com/problems/repeated-dna-sequences/

# 187. Repeated DNA Sequences
# Medium
# 3.2K
# 506
# Companies
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]


from collections import defaultdict
def repeated_dna(s: str) -> str:
    n=len(s)
    cnt=defaultdict(int)
    ans=[]
    for i in range(n-9):
        dna=s[i: i+10]
        cnt[dna] +=1
        if cnt[dna] == 2:
            ans.append(dna)
    return ans



if __name__ == "__main__":
    s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print ("{}".format(repeated_dna(s)))