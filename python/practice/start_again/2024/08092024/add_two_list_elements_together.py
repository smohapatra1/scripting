#   Add two list elements together

def AddList(list1, list2):
    sum = []
    for i in range(0, len(list1)):
        sum.append(list1[i] + list2[i])
    return sum

if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6] 
    result = AddList(list1, list2)
    print (result)
