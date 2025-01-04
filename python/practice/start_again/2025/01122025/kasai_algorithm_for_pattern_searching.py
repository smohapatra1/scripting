#   https://www.geeksforgeeks.org/kasais-algorithm-for-construction-of-lcp-array-from-suffix-array/

class Suffix:
	def __init__(self):
		self.index = 0
		self.rank = [0, 0]

def buildSuffixArray(txt, n):
	suffixes = [Suffix() for _ in range(n)]

	for i in range(n):
		suffixes[i].index = i
		suffixes[i].rank[0] = ord(txt[i]) - ord('a')
		suffixes[i].rank[1] = ord(txt[i + 1]) - ord('a') if i + 1 < n else -1

	suffixes.sort(key=lambda x: (x.rank[0], x.rank[1]))

	ind = [0] * n
	for k in range(4, 2 * n, k * 2) if 'k' in locals() and k > 0 else range(4, 2 * n, 1):
		rank = 0
		prev_rank = suffixes[0].rank[0]
		suffixes[0].rank[0] = rank
		ind[suffixes[0].index] = 0

		for i in range(1, n):
			if suffixes[i].rank[0] == prev_rank and suffixes[i].rank[1] == suffixes[i - 1].rank[1]:
				prev_rank = suffixes[i].rank[0]
				suffixes[i].rank[0] = rank
			else:
				prev_rank = suffixes[i].rank[0]
				suffixes[i].rank[0] = rank + 1
			ind[suffixes[i].index] = i

		for i in range(n):
			nextindex = suffixes[i].index + k // 2
			suffixes[i].rank[1] = suffixes[ind[nextindex]].rank[0] if nextindex < n else -1

		suffixes.sort(key=lambda x: (x.rank[0], x.rank[1]))

	suffixArr = [suffix.index for suffix in suffixes]
	return suffixArr

def kasai(txt, suffixArr):
	n = len(suffixArr)
	lcp = [0] * n
	invSuff = [0] * n

	for i in range(n):
		invSuff[suffixArr[i]] = i

	k = 0

	for i in range(n):
		if invSuff[i] == n - 1:
			k = 0
			continue

		j = suffixArr[invSuff[i] + 1]

		while i + k < n and j + k < n and txt[i + k] == txt[j + k]:
			k += 1

		lcp[invSuff[i]] = k

		if k > 0:
			k -= 1

	return lcp

# Utility function to print an array
def printArr(arr):
	print(" ".join(map(str, arr)))

# Driver program
if __name__ == "__main__":
	input_str = "banana"

	suffixArr = buildSuffixArray(input_str, len(input_str))
	n = len(suffixArr)

	print("Suffix Array:")
	printArr(suffixArr)

	lcp = kasai(input_str, suffixArr)

	print("\nLCP Array:")
	printArr(lcp)
