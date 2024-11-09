#   https://www.geeksforgeeks.org/problems/check-the-status/1

def CheckStatus(a, b , flag):
    if (a > 0 and b < 0 ) or (a < 0 and b > 0 ) and flag == 'False':
        return True
    elif (a < 0 and b < 0): 
        return True
    else:
        return False


if __name__ == "__main__":
    a = 1
    b = -1
    flag = 'False'
    print ("Status is : ", CheckStatus(a, b , flag))