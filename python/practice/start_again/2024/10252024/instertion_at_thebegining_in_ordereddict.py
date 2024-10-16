#   https://www.geeksforgeeks.org/python-insertion-at-the-beginning-in-ordereddict/?ref=leftbar-rightbar

from collections import OrderedDict
def Insert(ini_dict1, ini_dict2):
    # Solution - 01 
    # join=OrderedDict(list(ini_dict2.items())+ list(ini_dict1.items()))
    # return join
    # Solution - 02 
    iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])
    iniordered_dict.update({'manjeet': '3'})
    iniordered_dict.move_to_end('manjeet', last=False)
    return iniordered_dict


if __name__ == "__main__":
    ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
    ini_dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])
    print ("Final Result after instertion ", Insert(ini_dict1, ini_dict2))
