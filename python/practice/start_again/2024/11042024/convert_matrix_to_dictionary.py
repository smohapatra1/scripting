#   https://www.geeksforgeeks.org/python-convert-matrix-to-dictionary/

def MatDict(test_list):
    res = {idx + 1 : test_list[idx] for idx in range(len(test_list))}
    return res
if __name__ == "__main__":
    test_list = [[5, 6, 7], [8, 3, 2], [8, 2, 1]] 
    print ("Results after converting Matrix to Dict : ", MatDict(test_list))