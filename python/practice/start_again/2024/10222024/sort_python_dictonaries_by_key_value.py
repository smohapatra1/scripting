
def SortedD(d):
    print ("Current Dictionary    : " + str(d))
    myKeys = list(d.keys())
    myKeys.sort()
    sd = {i: d[i] for i in myKeys}
    return sd

if __name__ == "__main__":
    # d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}
    d = {2: 56, 1: 2, 5: 12, 4: 24}
    print ("Results after sorting : ", SortedD(d))