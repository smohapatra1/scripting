#   https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-alphabetically/

def ListAlphabetically(tup):
    # Solution - 01 
    # return (sorted(tup, key = lambda x:x[0]))
    # Solution - 02 
    tup.sort(key = lambda x:x[0])
    return tup
    
if __name__ == "__main__":
    tup = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]
    res = ListAlphabetically(tup)
    print (res)