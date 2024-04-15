# #   https://www.hackerrank.com/challenges/manipulative-numbers/problem?isFullScreen=true

# Suppose that  is a list of  numbers  and  is a permutation of these numbers, we say B is K-Manipulative if and only if:

#  is not less than , where  represents the XOR operator.

# You are given . Find the largest  such that there exists a K-manipulative permutation .

# Input:

# The first line is an integer . The second line contains  space separated integers - .

# Output:
# The largest possible , or  if there is no solution.

# Constraints:

# Sample Input 0

# 3
# 13 3 10
# Sample Output 0

# 2
# Explanation 0

# Here the list  is . One possible permutation . Here 
# .
# So there exists a permutation  of  such that  is not less than . However there does not exist any permutation  of  such that  is not less than . So the maximum possible value of  is .

# Sample Input 1

# 4
# 1 2 3 4
# Sample Output 1

# 1
# Explanation 1

# Here the list  is . One possible permutation . Here 
# .
# So there exists a permutation  of  such that  is not less than . However there does not exist any permutation  of  such that  is not less than . So the maximum possible value of  is .


import collections

def native_solver(arr):
    for k in range(100):
        cnt = collections.Counter([num >> k for num in arr])
        for elm in cnt:
            if cnt[elm] * 2 > len(arr):
                return k-1

def manipulativeNumbers(a):
    return native_solver(a)

if __name__ == "__main__":
    a_count = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = manipulativeNumbers(a)
    print (result)