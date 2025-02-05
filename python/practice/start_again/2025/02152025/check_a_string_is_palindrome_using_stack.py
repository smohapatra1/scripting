#   https://www.geeksforgeeks.org/check-whether-the-given-string-is-palindrome-using-stack/

stack = []
top = -1
def push(ele:str):
    global top
    top += 1
    stack[top] = ele
def pop():
    global top
    ele = stack[top]
    top -=1
    return ele
def palindrome(s:str) -> bool:
    global stack
    l = len(s)
    stack = ['0'] * (l+1)
    mid = l//2
    i = 0 
    while i < mid:
        push (s[i])
        i +=1
    if l % 2 != 0:
        i +=1
    while i < l :
        ele = pop()
        if ele != s[i]:
            return False
        i +=1
    return True

if __name__ == "__main__":
    s = "madam"
    if palindrome(s):
        print ("yes")
    else:
        print ("no")