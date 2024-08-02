# Write a Python program to find the common elements between two lists.

def Common(list_a, list_b):
    common_element = []
    for i in list_a:
        if i in list_b:
            common_element.append(i)
    return common_element
            


if __name__ == "__main__":
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = Common(list_a, list_b)
    print (result)