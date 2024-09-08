#   https://www.geeksforgeeks.org/python-program-to-find-minimum-number-of-rotations-to-obtain-actual-string/

def findRotation(str1, str2):
    lr = 0 
    rr = 0
    m = str1 
    while True:
        m = m[len(m)-1] + m[:len(m)-1]
        if m == str2:
            lr +=1
            break
        else:
            lr +=1
            if lr > len(str2):
                break
    while True:
        str1 = str1[1:len(str1)] + str1[0]
        if str1 == str2:
            rr +=1
            break
        else:
            rr +=1
            if rr > len(str2):
                break
    if lr < len(str2):
        print (min(lr, rr))
    else:
        print ("Given strings {} and {} are not of same kind".format(str1, str2))



if __name__ == "__main__":
    str1 = 'sgeek'
    str2 = 'geeks'
    # str1 = 'eksge'
    # str2 = 'geeks'
    findRotation(str1, str2)