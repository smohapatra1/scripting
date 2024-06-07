#   Counting Special Characters in a String

import re
spl = "!@#$%^&*()"

count = re.sub('[\w]+', '', spl)
print (len(count))