#   https://www.geeksforgeeks.org/problems/regex-python/1

import re
def Extract(s):
    # return re.findall(r'\d+', s)
    return [int(n) for n in re.findall(r'\d+', s)]
    
if __name__ == "__main__":
    # s = "asdasd123asmdasdk34234kfdsd34sdfk5"
    s = "There are 3 numbers in this string: 1, 2, and 3."
    print("Results after extracting Numbers : ", Extract(s))