from collections import Counter

a = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4]
print (Counter(a))
#Using counters on strings
print (Counter('aaaaababbabajahajaajjaaja'))
#Counters on sentences 
b = "I am a Goooddddddddd BOY BOY "
print (Counter(b.split()))
#getting the lower case 
print (Counter(b.lower().split()))
c = Counter(b)
print (c.most_common(2))
print (list(c))