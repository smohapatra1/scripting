# #   https://www.hackerrank.com/challenges/prime-digit-sums/problem?isFullScreen=true

# Chloe is fascinated by prime numbers. She came across the number  on a sign and, though the number is not prime, found some primes hiding in it by using the following rules:

# Every three consecutive digits sum to a prime:
# Every four consecutive digits sum to a prime:
# Every five consecutive digits sum to a prime:
# You must answer  queries, where each query consists of an integer, . For each , find and print the number of positive -digit numbers, modulo , that satisfy all three of Chloe's rules (i.e., every three, four, and five consecutive digits sum to a prime).

# Input Format

# The first line contains an integer, , denoting the number of queries.
# Each of the  subsequent lines contains an integer denoting the value of  for a query.

# Constraints

# Output Format

# For each query, print the number of -digit numbers satisfying Chloe's rules, modulo , on a new line.

# Sample Input 0

# 1
# 6
# Sample Output 0

# 95
# Explanation 0

# There are  six-digit numbers satisfying the property above, where the respective first and last ones are  and .


mod = 10**9 + 7
A = [0,0,0,0,0,2,3,15,2,0]
B = [0,0,0,0,0,4,9,13,17,2]
results = [1,9,90,303,280,218,95,101,295]
for _ in range(int(input())):
   n = int(input())
   for i in range(len(A),n):
      A.append((2*(A[i-5] + B[i-5])) % mod)
      B.append((A[i-1] + A[i-5] + 2*B[i-5]) % mod)
   print(results[n] if n < 9 else
      (5*A[n-1] + 9*A[n-2] + 19*A[n-3] + 6*A[n-4] + 3*A[n-5]
      + 2*B[n-1] + 5*B[n-2] + 20*B[n-3] + 5*B[n-4] + 4*B[n-5]) % mod)