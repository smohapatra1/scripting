# #   https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=false


# You are given a string .
# Your task is to find out whether  is a valid regex or not.

# Input Format

# The first line contains integer , the number of test cases.
# The next  lines contains the string .

# Constraints


# Output Format

# Print "True" or "False" for each test case without quotes.

# Sample Input

# 2
# .*\+
# .*+
# Sample Output

# True
# False
# Explanation

# .*\+ : Valid regex.
# .*+: Has the error multiple repeat. Hence, it is invalid.

import re
if __name__ == "__main__":
    s=int(input().strip())
    for _ in range(s):
        try:
            re.compile(input().strip())
            res=True
        except BaseException:
            res=False
        print (res)
    