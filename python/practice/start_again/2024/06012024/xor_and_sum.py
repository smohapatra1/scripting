# #   https://www.hackerrank.com/challenges/xor-and-sum/problem?isFullScreen=true

# You are given two positive integers  and  in binary representation. You should find the following sum modulo :

# where operation  means exclusive OR operation, operation  means binary shift to the left.

# Please note, that we consider ideal model of binary integers. That is there is infinite number of bits in each number, and there are no disappearings (or cyclic shifts) of bits.

# Input Format

# The first line contains number   in binary representation. The second line contains number   in the same format. All the numbers do not contain leading zeros.

# Output Format

# Output a single integer  the required sum modulo .

# Sample Input

# 10
# 1010
# Sample Output

# 489429555

def xorAndSum(a, b ):
    mod = 10 ** 9 + 7 
    a = int(a, 2)
    b = int(b, 2)
    sum = 0 
    for i in range(314160):
        sum +=(a^b<<i)
    return sum % mod 

if __name__ == "__main__":
    a = input()
    b = input()
    result = xorAndSum(a, b )
    print (result)