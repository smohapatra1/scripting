#   https://www.geeksforgeeks.org/python-remove-leading-zeros-ip-address/

import re
def RemoveLeadingZero(s):
    x = re.sub(r'\b0+(\d)', r'\1', s)
    return x

if __name__ == "__main__":
    s = "001.200.001.004"
    s1 = "100.020.003.400"
    print (RemoveLeadingZero(s))
    print (RemoveLeadingZero(s1))