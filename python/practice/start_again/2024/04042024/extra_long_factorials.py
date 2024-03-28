# #   https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true


# The factorial of the integer , written , is defined as:

# Calculate and print the factorial of a given integer.

# For example, if , we calculate  and get .

# Function Description

# Complete the extraLongFactorials function in the editor below. It should print the result and return.

# extraLongFactorials has the following parameter(s):

# n: an integer
# Note: Factorials of  can't be stored even in a  long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.

# We recommend solving this challenge using BigIntegers.

# Input Format

# Input consists of a single integer 

# Constraints


# Output Format

# Print the factorial of .

# Sample Input


# Sample Output


# Explanation

def extraLongFact(n):
    res = 1 
    while (n!=1):
        res*=n
        n-=1
    print (res)


if __name__ == "__main__":
    n=int(input())
    result=extraLongFact(n)
    # print (result)