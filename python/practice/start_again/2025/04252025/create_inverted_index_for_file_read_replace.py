#   https://www.geeksforgeeks.org/create-inverted-index-for-file-using-python/

punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

for ele in read:
    if ele in punc:
        read = read.replace(ele, " ")
read
read = read.lower()
read
