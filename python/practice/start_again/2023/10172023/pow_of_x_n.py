# <!-- #   https://leetcode.com/problems/powx-n/

# 50. Pow(x, n)
# Medium
# 8.9K
# 8.7K
# Companies
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25 -->


def pow(x: float , n=int) -> float:
    def calculate(base=x, exponent=abs(n)):
        if exponent == 0:
            return 1
        elif exponent %2 == 0 :
            return calculate( base * base , exponent//2)
        else:
            return base * calculate( base * base , (exponent - 1)//2)
    
    f=calculate()
    return float(f) if n >= 0 else 1/f




if __name__ == "__main__":
    # x = 2.00000
    # n = 10
    #x = 2.10000
    #n = 3
    x = 2.00000
    n = -2
    print ("{}".format(pow(x,n)))
