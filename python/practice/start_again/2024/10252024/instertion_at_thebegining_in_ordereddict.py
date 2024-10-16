#   https://www.geeksforgeeks.org/python-insertion-at-the-beginning-in-ordereddict/?ref=leftbar-rightbar

from collections import OrderedDict
def Insert(ini_dict1, ini_dict2):
    join=OrderedDict(list(ini_dict2.items())+ list(ini_dict1.items()))
    return join


if __name__ == "__main__":
    ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
    ini_dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])
    print ("Final Result after instertion ", Insert(ini_dict1, ini_dict2))
