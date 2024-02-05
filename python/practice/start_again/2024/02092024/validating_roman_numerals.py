# #   https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=false

# You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

# Input Format

# A single line of input containing a string of Roman characters.

# Output Format

# Output a single line containing True or False according to the instructions above.

# Constraints

# The number will be between  and  (both included).

# Sample Input

# CDXXI
# Sample Output

# True
# References

# Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

# https://developers.google.com/edu/python/regular-expressions

import re 

if __name__ == "__main__":
    regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"	# Do not delete 'r'.
    print(str(bool(re.match(regex_pattern, input()))))