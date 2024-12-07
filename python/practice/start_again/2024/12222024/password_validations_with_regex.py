#   https://www.geeksforgeeks.org/problems/regular-expressions-2-python/1

# password validation rules 
# The validation rules are as follows:

# The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
# In any other case the string is not valid.
import re
def PasswordValidate(s):
    pattern = r'^[a-z][!@#$%]\d+$'
    if re.match(pattern, s):
        return True
    return False
if __name__ == "__main__":
    # s = "asdsab@!@234"
    s = 'a!12345'
    print (PasswordValidate(s))