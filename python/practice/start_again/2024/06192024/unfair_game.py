# #   https://www.hackerrank.com/challenges/unfair-game/problem?isFullScreen=true

# You are playing a game of Nim with a friend. The rules are are follows:

# 1) Initially, there are N piles of stones. Two players play alternately.

# 2) In each turn, a player can choose one non empty pile and remove any number of stones from it. At least one stone must be removed.

# 3) The player who picks the last stone from the last non empty pile wins the game.

# It is currently your friend's turn. You suddenly realize that if your friend was to play optimally in that position, you would lose the game. So while he is not looking, you decide to cheat and add some (possibly 0) stones to each pile. You want the resultant position to be such that your friend has no guaranteed winning strategy, even if plays optimally. You cannot create a new pile of stones. You can only add stones, and not remove stones from a pile. What is the least number of stones you need to add?

# Input Format

# The first line contains the number of cases T. T cases follow. Each case contains the number N on the first line followed by N numbers on the second line. The ith number denotes si, the number of stones in the ith pile currently.

# Constraints

# 1 <= T <= 20

# 2 <= N <= 15

# 1 <= si < 1000000000 (10^9)

# Output Format

# Output T lines, containing the answer for each case. If the current position is already losing for your friend, output 0.

# Sample Input

# 3

# 2

# 1 3

# 3

# 1 1 1

# 4

# 10 4 5 1

# Sample Output

# 2

# 3

# 6

# Explanation

# For the first case, add 2 stones to the first pile. Then, both piles will have 3 stones each. It is easy to verify that your friend cannot win the game unless you make a mistake.

# For the second case, add 1 stone to the first pile, and 2 stones to the second pile.


import operator
from functools import reduce

def xor(nums):
    return reduce(operator.xor, nums, 0)

def lowZero(v):
    """position of the lowest 0"""
    p = 0
    while True:
        m = 1 << p
        if v & m == 0:
            return p
        p += 1

def highOne(v):
    """position of the highest 1"""
    p = 0
    high = None
    while v != 0:
        m = 1 << p
        if v & m != 0:
            high = p
            v &= ~m
        p += 1
    return high

def zeroAt(v, p):
    """true if v has 0 at position p"""
    return v & (1 << p) == 0

def diffToFlip(v, p):
    """how much to add to flip the bit at p and clear below it"""
    t = 1 << p
    r = (v + t) & ~(t - 1)
    return r - v

def lowPosWithMoreThanOneZero(nums):
    """lowest position where more than one number has 0"""
    p = 0
    while True:
        m = 1 << p
        n = sum(1 if v & m == 0 else 0 for v in nums)
        if n > 1:
            return p
        p += 1
    
def pairs(n):
    return ((i, j) for i in range(0, n - 1) for j in range(i + 1, n))

"""pile fixers"""
                    
def fixPiles(piles):
    """add minimum number of counters to piles to make them a staple nim position"""
    highOneP = highOne(xor(piles))
    if highOneP == None: # the piles are in a winning position
        r = piles
    elif any(zeroAt(v, highOneP) for v in piles):
        r = fixPilesWithZeroAtHigh(piles)
    else:
        r = fixPilesWithoutZeroAtHigh(piles, highOneP)
    return r

def fixPilesWithZeroAtHigh(piles):
    """fix piles that have a pile with zero at the high 1-bit position"""
    piles = list(piles)
    while True:
        highOneP = highOne(xor(piles))
        """see if the piles are fixed to a winning position"""
        if highOneP == None:
            return piles
        """choose a pile with 0 at the high 1 position with min to add to flip that 0"""
        candidates = [(i, diffToFlip(v, highOneP)) for i, v in enumerate(piles) if zeroAt(v, highOneP)]
        winner = min(candidates, key = operator.itemgetter(1))
        """add to the winning pile"""
        i, add = winner
        piles[i] += add
    return piles

def fixPilesWithoutZeroAtHigh(piles, highOneP):
    """fix piles that do not have a pile with zero at the high 1-bit position"""
    """high piles are piles' bits above highOneP"""
    highPiles = [v >> (highOneP + 1) for v in piles]
    """decorate each high pile the position of the first 0, same as the number
    of trailing ones"""
    highPilesZ = [(v, lowZero(v)) for v in highPiles]
    """find pairs with matching trailing ones; each match is a 3-tuple of two pile
    indices and the position of the zero"""
    matches = [(i, j, highOneP + 1 + highPilesZ[i][1]) for i, j in pairs(len(piles)) if highPilesZ[i][1] == highPilesZ[j][1]]
    """if there are pairs with matching trailing ones find the lowest position with
    at least two zeros; each pair of piles in this set is a matching pair"""
    if not matches:
        zeroP = lowPosWithMoreThanOneZero(highPiles)
        lowzs = [i for i, v in enumerate(highPiles) if zeroAt(v, zeroP)]
        nz = len(lowzs)
        baseZeroP = highOneP + 1 + zeroP
        matches = [(lowzs[i], lowzs[j], baseZeroP) for i, j in pairs(nz)]
    """for each pair add to flip the matching zeros and fix resulting piles with the
    zero-at-high-1 fixer; then choose the best result out of all pairs"""
    results = (fixPilesTwoZeros(piles, zeroP, i, j) for i, j, zeroP in matches)
    return min(results, key = sum)

def fixPilesTwoZeros(piles, zeroP, i, j):
    """given a set of piles where piles i, j have zeros at zeroP add to each pile to flip that zero and
    then fix the piles"""
    iAdd = diffToFlip(piles[i], zeroP)
    jAdd = diffToFlip(piles[j], zeroP)
    piles = list(piles)
    piles[i] += iAdd
    piles[j] += jAdd
    return fixPilesWithZeroAtHigh(piles)

def solve(piles):
    fixedPiles = fixPiles(piles)
    return sum(fixedPiles) - sum(piles), fixedPiles

def readLine(): return input()
def readInt(): return int(readLine())
def readInts(): return tuple(int(token) for token in readLine().split())
def readIntList(): return list(readInts())

def main():
    nt = readInt()
    for _ in range(nt):
        _n = readInt()
        piles = readIntList()
        answer, _fixedPiles = solve(piles)
        print(answer)
main()