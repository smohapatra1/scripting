#   https://www.geeksforgeeks.org/built-in-modules-in-python/

import re 

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
text = "Contact us at info@example.com and support@example.org for more details."
match = re.search(pattern, text)
if match :
    print ("First found email : ", match.group())
emails = re.findall(pattern, text)
print ("All found email:", emails)