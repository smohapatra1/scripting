#   https://www.geeksforgeeks.org/python-set-difference-find-lost-element-duplicated-array/

def LostElement(A,B):
    # c = []
    # for i in A:
    #     if i not in B:
    #         c.append(i)
    # return c

    # Solution -02 
    A = set(A)
    B = set(B)
    if len(A) > len(B):
        return list(A-B)
    else:
        return list(B-A)

if __name__ == "__main__":
    A = [1, 2, 10, 4, 5, 7, 9]
    B = [4, 5, 7, 9]
    print ("Results after finding lost element : ", LostElement(A, B ))