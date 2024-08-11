#   https://www.geeksforgeeks.org/find-sum-and-average-of-list-in-python/

def SumAvg(list):
    # count = 0 
    # for i in list:
    #     count = count + i
    # avg = count/len(list)
    # print ("sum = ", count )
    # print ("avg = ", avg)

    #Solution 2 
    count = sum(list)
    avg = count/ len(list)
    print ("sum = ", count )
    print ("avg = ", avg)

if __name__ == "__main__":
    list = [ 1, 5, 10 , 10 , 1, 2]
    result = SumAvg(list)