#   https://www.geeksforgeeks.org/python-program-to-find-all-the-combinations-in-the-list-with-the-given-condition/

from itertools import combinations

def Combinations(test):
    idx = 0 
    tmp = combinations(test, 2)
    for i in list(tmp):
        idx = idx + 1
        print ("Combination", idx , ": ", i ) 

if __name__ == "__main__":
    test = [1,2,3] 
    result = Combinations(test)
    print (result)

