#   Write a Python program to remove duplicates from a list.


def RemoveDupe(n):
    unique = []
    for i in n:
        if i not in unique:
            unique.append(i)
    return unique

if __name__ == "__main__":
    n = [ 1, 1, 4, 5, 1]
    # n = [ 2,2, 4, 5, 2]
    result = RemoveDupe(n)
    print (result)