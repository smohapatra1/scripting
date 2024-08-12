# https://www.geeksforgeeks.org/python-program-to-print-odd-numbers-in-a-list/

def Odd(lst):
    # Solution 1
    # for i in lst:
    #     if i % 2 != 0:
    #         print (i, end= ' ')
    # Solution 2 
    ans = [ num for num in lst if num % 2 != 0 ]
    print (ans)

if __name__ == "__main__":
    lst = [ 1, 5, 6, 8, 10, 12]
    result = Odd(lst)