#   https://www.geeksforgeeks.org/python-sum-of-number-digits-in-list/?ref=leftbar-rightbar

def SumOfNums(list):
    res = []
    for i in list:
        sum = 0 
        for digit in str(i):
            sum += int(digit)
        res.append(sum)
    return res 
if __name__ == "__main__":
    list = [ 1, 10 , 19 , 16 , 17, 18 ]
    result = SumOfNums(list)
    print (result)