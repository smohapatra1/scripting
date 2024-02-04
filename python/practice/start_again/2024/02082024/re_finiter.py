import re 
s=re.finditer(r'\w', 'http://www.hackerrank.com/')
print (s)
q=map(lambda x:x.group(), re.finditer(r'\w', 'http://www.hackerrank.com/'))
print (q)