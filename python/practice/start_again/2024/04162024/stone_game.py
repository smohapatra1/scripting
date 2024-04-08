# #   https://www.hackerrank.com/challenges/stonegame/problem?isFullScreen=true

# Alice and Bob are playing the game of Nim with  piles of stones with sizes . If Alice plays first, she loses if and only if the 'xor sum' (or 'Nim sum') of the piles is zero, i.e., .

# Since Bob already knows who will win (assuming optimal play), he decides to cheat by removing some stones in some piles before the game starts. However, to reduce the risk of suspicion, he must keep at least one pile unchanged. Your task is to count the number of ways Bob can remove the stones to force Alice into losing the game. Since the number can be very large, output the number of ways modulo . Assume that both players will try to optimize their strategy and try to win the game.

# Input Format

# The first line of the input contains an integer  denoting the number of piles. The next line contains  space-separated integers  indicating the sizes of the stone piles.

# Constraints

# Output Format

# Print a single integer denoting the number of ways Bob can force Alice to lose the game, modulo .

# Sample Input 0

# 3
# 1 2 3
# Sample Output 0

# 4
# Explanation 0

# The answer is . The four possible resulting lists of piles is:

# Note that  is not allowed since he must keep one pile unchanged.

# Sample Input 1

# 10
# 10 10 1 1 1 1 1 10 10 10
# Sample Output 1

# 321616


modulus = int(1e9 + 7)

def prodsums(arr):
    n = len(arr)+1
    s = [[0 for i in range(n)] for j in range(n)]
    s[0][0] = 1
    for i in range(1,n):
        s[i][0] = 1 
        for j in range(1,n):
            s[i][j] = (s[i-1][j] + arr[i-1] * s[i-1][j-1]) % modulus
    return [s[n-1][j] for j in range(n)]

def calcbit(piles, xorpiles, k):
    if xorpiles >> (k+1):
        return 0
    m = (1 << k) - 1
    evens = [p & m for p in piles if ((p >> k) & 1) == 0]
    odds = [p & m for p in piles if (p >> k) & 1]
    osz = len(odds)
    if osz == 0:
        return 0
    psum = prodsums(odds)
    b = 1
    for e in evens:
        b *= e
    s = 0
    for sz in range(0, osz, 2):
        pw = (1 << (k * (osz - sz - 1))) % modulus
        s += pw * psum[sz]
    return (b * s) % modulus 

def xorless(piles):
    orp = 0
    xorp = 0
    for p in piles:
        orp |= p
        xorp ^= p
    k = 0
    result = 0
    while (1 << k) <= orp:
        result = (result + calcbit(piles, xorp, k)) % modulus
        k += 1
    return result

def stoneGame(p):
    p2 = [x+1 for x in p]
    a = xorless(p2)
    b = xorless(p)
    return (a + modulus - b) % modulus

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    p_count = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = stoneGame(p)
    print (result)

    # fptr.write(str(result) + '\n')

    # fptr.close()