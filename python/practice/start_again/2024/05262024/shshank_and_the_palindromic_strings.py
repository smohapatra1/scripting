# #   https://www.hackerrank.com/challenges/shashank-and-palindromic-strings/problem?isFullScreen=true


# Shashank loves strings, but he loves palindromic strings the most. He has a list of  strings, , where each string, , consists of lowercase English alphabetic letters. Shashank wants to count the number of ways of choosing non-empty subsequences  such that the following conditions are satisfied:

#  is a subsequence of string ,  is a subsequence of string ,  is a subsequence of string , , and  is a subsequence of string .
#  is a palindromic string, where + denotes the string concatenation operator.
# You are given  queries where each query consists of some list, . For each query, find and print the number of ways Shashank can choose  non-empty subsequences satisfying the criteria above, modulo , on a new line.

# Note: Two subsequences consisting of the same characters are considered to be different if their characters came from different indices in the original string.

# Input Format

# The first line contains a single integer, , denoting the number of queries. The subsequent lines describe each query in the following format:

# The first line contains an integer, , denoting the size of the list.
# Each line  of the  subsequent lines contains a non-empty string describing .
# Constraints

#  over a test case.
# For  of the maximum score:

#  over a test case.
# Output Format

# For each query, print the number of ways of choosing non-empty subsequences, modulo , on a new line.

# Sample Input 0

# 3
# 3
# aa
# b
# aa
# 3
# a
# b
# c
# 2
# abc
# abc
# Sample Output 0

# 5
# 0
# 9
# Explanation 0

# The first two queries are explained below:

# We can choose the following five subsequences:

# , , , where  is the first character of  and  is the first character of .
# , , , where  is the second character of  and  is the second character of .
# , , , where  is the first character of  and  is the second character of .
# , , , where  is the second character of  and  is the first character of .
# , , 
# Thus, we print the result of  on a new line.

# There is no way to choose non-empty subsequences such that their concatenation results in a palindrome, as each string contains unique characters. Thus, we print  on a new line.

import sys 

pali_memo = {}

def palindrome_count(data):
	global pali_memo

	if data in pali_memo:
		return pali_memo[data]

	pairs = [(i,j,)for(i,a,)in enumerate(data)

	for j in range(i+1,len(data))if a==data[j]]

	intermediates = [j - i - 1 for (i,j,) in pairs]

	table = [[0,]*len(pairs)for pair in pairs]
	for (I,(i,l,),) in enumerate(pairs):
		for (J,(j,k,),) in enumerate(pairs):
			table[I][J] = (i < j) and (k < l)


	occurrences = [1 for pair in pairs]

	def f(k, d = {},):
		if k in d:
			L = d[k]
			for i in range(len(pairs)):
				occurrences[i] += L[i]
			return
		enclosed = table[k]
		L = occurrences[:]
		for j in range(k+1,len(pairs)):
			if enclosed[j]:
				occurrences[j] += 1
				f(j)
		d[k] = [new - old for (new,old,) in zip(occurrences,L)]

	for k in range(len(pairs)):
		f(k)

	evens = sum(occurrences)
	odds = (
		len(data) + sum(occurrence*intermediate
			for (occurrence,intermediate,) in zip(occurrences,intermediates,)))

	total = (evens + odds) % 1000000007

	pali_memo[data] = total

	return total

count_memo = {}

def pali(s):
	len_s = len(s)

	if len_s <= 0:
		return 1

	s_hash = '.'.join(s)

	if s_hash in count_memo:
		return count_memo[s_hash]

	if len_s == 1:
		count = palindrome_count(s[0])
		count_memo[s_hash] = count
		return count

	total = 0

	h2 = {}
	for key, value in enumerate(s[-1]):
		if value not in h2:
			h2[value] = [key]
		else:
			h2[value] += [key]

	for first in range(len(s[0])):
		if s[0][first] in h2:
			for last in h2[s[0][first]]:

				remaining = s[1:-1]
				left = s[0][first + 1:]
				right = s[-1][:last]

				left = [left] if left else []
				right = [right] if right else []

				total += pali(remaining)
				if right:
					total += pali(remaining + right)
				if left:
					total += pali(left + remaining)
				if right and left:
					total += pali(left + remaining + right)

	total = total % 1000000007
	count_memo[s_hash] = total
	return total

Q = int(input())
for q in range(Q):
	N = int(input())

	s = []
	for n in range(N):
		s += [input().strip()]

	print(pali(s) % 1000000007)