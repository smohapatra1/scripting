#   https://www.geeksforgeeks.org/python/check-if-two-pdf-documents-are-identical-with-python/

import hashlib
from difflib import SequenceMatcher

def hash_file(file1, file2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()
    with open(file1, "rb") as f1:
        chunk = 0 
        while chunk != b'':
            chunk = f1.read(1024)
            h1.update(chunk)
    with open(file2, "rb") as f2:
        chunk = 0 
        while chunk != b'':
            chunk = f2.read(1024)
            h2.update(chunk)
        return h1.hexdigest(), h2.hexdigest()
msg1, msg2 = hash_file("pd1.pdf", "pd2.pdf")

if (msg1 != msg2 ):
    print ("These files are not identical")
else:
    print ("These files are identical")
        


