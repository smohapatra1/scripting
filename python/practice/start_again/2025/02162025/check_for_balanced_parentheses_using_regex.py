#   https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/

import re
s = "(())()"
while re.search(r'\(\)', s):  
    s = re.sub(r'\(\)', '', s)
print("Balanced" if not s else "Unbalanced")