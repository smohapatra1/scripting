#   https://www.geeksforgeeks.org/python-check-url-string/

def CheckURL(s):
    x = s.split()
    res = []
    for i in x:
        if i.startswith("https:") or i.startswith("http"):
            res.append(i)
    return res
    
if __name__ == "__main__":
    s = 'My Profile: https://auth.geeksforgeeks.org/user/xyx%20xa/articles in the portal of https://www.geeksforgeeks.org/'
    print (CheckURL(s))