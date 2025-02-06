#   https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/

s = "{[()()]}"
st = []  
for c in s:
       # Push opening brackets onto the stack
    if c in '({[': 
        st.append(c)
    # Check for matching closing bracket
    elif c in ')}]':  
        if not st or (c == ')' and st[-1] != '(') or (c == '}' and st[-1] != '{') or (c == ']' and st[-1] != '['):
            print(False)  # Mismatched bracket
            break
        st.pop()  # Pop matched opening bracket
else:
    print(True if not st else False)  # Balanced if stack is empty

