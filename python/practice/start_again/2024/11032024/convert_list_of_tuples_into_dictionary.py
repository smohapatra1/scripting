#   https://www.geeksforgeeks.org/python-convert-a-list-of-tuples-into-dictionary/

def TupleDict(tups):
    res = {}
    for a, b in tups:
        res.setdefault(a, []).append(b)
    return res
    
if __name__ == "__main__":
    tups = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
    print ("Results after converting : ", TupleDict(tups))