# #   https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=false

# You are given a string .
#  contains alphanumeric characters only.
#  Your task is to sort the string  in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Input Format

# A single line of input contains the string .

# Constraints

# Output Format

# Output the sorted string .

# Sample Input

# Sorting1234
# Sample Output

# ginortS1324

if __name__ == "__main__":
    s=input().strip()
    print (*sorted(s, key=lambda x: (-x.islower(), x.isdigit() - x.isupper(), x in '02468', x)), sep='')