
def SortedD(d):
    print ("Current Dictionary    : " + str(d))
    myKeys = list(d.keys())
    myKeys.sort()
    sd = {i: d[i] for i in myKeys}
    return sd

if __name__ == "__main__":
    d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}
    print ("Results after sorting : ", SortedD(d))