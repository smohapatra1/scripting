#   https://www.geeksforgeeks.org/python-list-exercise/
#   https://www.geeksforgeeks.org/how-to-count-unique-values-inside-a-list/

from collections import Counter

def UniqueList(input_list):
    # l1 = []
    # count = 0 
    # for i in input_list:
    #     if i not in l1:
    #         count = count +1
    #         l1.append(i)
    # print ("{} = Total {}".format(l1, count))

    # Solution - 2 
    item = Counter(input_list).keys()
    print ("Keys {} and total count {}".format(item, len(item)))


if __name__ == "__main__":
    input_list = [1, 2, 2, 5, 8, 4, 4, 8]
    UniqueList(input_list)
