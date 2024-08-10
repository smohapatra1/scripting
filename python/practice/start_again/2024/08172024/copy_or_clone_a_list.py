#   https://www.geeksforgeeks.org/python-cloning-copying-list/

def Clone(list):
    new_list = list[:]
    return new_list

if __name__ == "__main__":
    list = [ 1 , 4, 6, 4, 1, 3]
    result = Clone(list)
    print (result)