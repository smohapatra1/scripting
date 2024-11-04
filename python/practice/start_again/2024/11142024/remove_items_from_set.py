#   https://www.geeksforgeeks.org/python-remove-items-set/
def RemoveSet(initial_set):
    # Solution - 1 
    while initial_set:
        initial_set.pop()
        print(initial_set)
        
    # Solution - 2
    # while initial_set:
    #     initial_set.discard(max(initial_set))
    #     print (initial_set)
    
if __name__ == "__main__":
    initial_set = set([12, 10, 13, 15, 8, 9])
    RemoveSet(initial_set)

