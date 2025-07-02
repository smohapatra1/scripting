#   You have to find if the string is K-palindrome or not. Can you do that? 
#   https://www.google.com/search?q=You+have+to+find+if+the+string+is+K-palindrome+or+not.+Can+you+do+that%3F+python&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNbNzlVHsfMLfk3ceLEp9Bs0672SA%3A1751483035626&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZud1z6kQpMfoEdCJxnpm_3W-pLdZZVzNY_L9_ftx08kwv-_tUbRt8pOUS8_MjaceHuSAD6YvWZ0rfFzwmtmaBgLepZn2IJkVH-w3cPU5sPVz9l1Pp06apNShUnFfpGUJOF8p91U6HxH3ukND0OVTTVy0CGuHNdViLZqynGb0mLSRGeGVO46qnJ_2yk3F0uV6R6BW9rQ&aep=1&ntc=1&sa=X&ved=2ahUKEwiLuqzh7p6OAxVdI0QIHUguJPkQ2J8OegQIFxAC&biw=1729&bih=876&dpr=2&mstk=AUtExfDGUV8QWCOXfSbpdsKsOlfCO0rbDp2KLee_xC3PwSkVcdjzYhWOarAMWwEfjl6UvY5bDsOGGLcDuTHoDVVFh5dzfYVs8MWV_583feuic9LZpw7sEoRG4mPRPPjjdHbMwsqLxAAhHIEY2cX08naB_osxTxMmZ_OSZTlxIGWZFDdghHL13K_-kk-h4gekeGeVtW5JcUmj6hbUPQnRWV6Xy1LM_e54DPUuRvED2Y7CZxp_6Us2IhaR-2Ip5OkduK8NMAYKBJ4NVmk_LGxNwLMd_3krD9KqBPhAQmHv88McBkT8pCQGJ_-FzpJ6mD6XkMxX3h0SttbjUBcXPhUJovaa9wm7Ql5rp-gXSTRZENmX1ZJm4cXftfRz6b2kQD8REN9M8B_LXbLYnJ9bwHrWvSGf-hVHEHBsgEBebbg7_l1kfRgrpZKQRNoDIG-2rPrIaAUt5bM02NfDVgI&csuir=1

def isKPalRec(str1, str2, m, n):
    if not m: return n
    if not n: return m
    if str1[m-1] == str2[n-1]:
        return isKPalRec(str1, str2, m-1, n-1)
    res = 1 + min(isKPalRec(str1, str2, m-1, n),  # Remove from str1
                 (isKPalRec(str1, str2, m, n-1))) # Remove from str2
                 
    return res
def isKPal(string, k):
    revStr = string[::-1]
    l = len(string)

    return (isKPalRec(string, revStr, l, l) <= k * 2)


# Driver program
string = "acdcb"
k = 2

print("Yes" if isKPal(string, k) else "No")
