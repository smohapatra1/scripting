#   https://www.geeksforgeeks.org/categorize-password-as-strong-or-weak-using-regex-in-python/

def PasswordCheck(s):
    if 9 <= len(s) <= 20 :
        if re.search(r'(.)\1\1', s):
            return "Weak Password : Same chars repeated more time in a row"
        if re.search(r'(..)(.*?)\1', s):
            return "Weak Password : Same string pattern repetition"
        else:
            return "Strong Password"
    elif s == "\n" or s == " ":
        return "Weak Password : Password shouldn't have newline and spaces "
    else:
        return "Weak Password : Password must be >9 and < 20 chars"

    

if __name__ == "__main__":
    s = "Qggf!@ghf3"
    s1 = "aaabnil1gu"
    s2 = "Aasd!feasnm"
    s3 = "772*hdf77"
    s4 = " "
    s5 = "test"
    print (PasswordCheck(s))
    print (PasswordCheck(s1))
    print (PasswordCheck(s2))
    print (PasswordCheck(s3))
    print (PasswordCheck(s4))
    print (PasswordCheck(s5))