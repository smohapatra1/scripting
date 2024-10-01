#   https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-by-second-item/

def Sort(tup):
    tup.sort(key = lambda x:x[1])
    return tup
if __name__ == "__main__":
    tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)] 
    result = Sort(tup)
    print (result)