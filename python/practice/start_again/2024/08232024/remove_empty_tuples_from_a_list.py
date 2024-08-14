#   https://www.geeksforgeeks.org/python-remove-empty-tuples-list/

def RemoveTuples(n):
    n = [ t for t in n if t]
    return n

if __name__ == "__main__":
    n = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]
    r = RemoveTuples(n)
    print (r)
                                                                                     
