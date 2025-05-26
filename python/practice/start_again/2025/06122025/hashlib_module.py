#   https://www.geeksforgeeks.org/built-in-modules-in-python/

import hashlib
messages = "Hello"
hashed = hashlib.sha256(messages.encode()).hexdigest()
print (hashed)