#   https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/

def InterChange(my_list):
    print ("Current list = ", my_list)
    my_list[0], my_list[-1] =  my_list[-1], my_list[0]
    return my_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print ("After swap   = ", InterChange(my_list))