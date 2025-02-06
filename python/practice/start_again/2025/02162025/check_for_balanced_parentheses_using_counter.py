#   https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/

counter = 0 
s = "{[()()]}"
for ch in s :
    if ch == '(':
        counter +=1 
    elif ch == ')':
        counter -=1
    if counter < 0:
        print ("Unbalanced")
        break
if counter == 0:
    print ("Balanced")
else:
    print ("Unbalanced")

