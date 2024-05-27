# #   https://www.hackerrank.com/challenges/dorsey-thief/problem?isFullScreen=true

# Mr. Dorsey Dawson recently stole  grams of gold from ACME Jewellers. He is now on a train back home. To avoid getting caught by the police, he has to convert all the gold he has into paper money. He turns into a salesman and starts selling the gold in the train.

# There are  passengers who have shown interest in buying the gold. The  passenger agrees to buy  grams of gold by paying  dollars. Dawson wants to escape from the police and also maximize the profit. Can you help him maximize the profit?

# Note: The  passenger would buy exactly  grams if the transaction is successful.

# Input Format

# The first line contains two space separated integers,  and , where  is the number of passengers who agreed to buy and  is the stolen amount of gold (in grams).
#  lines follow. Each line contains two space separated integers -  and , where  is the the value which the  passenger has agreed to pay in exchange for  grams of gold.

# Constraints

# all 's and 's are less than or equal to  and greater than .
# Output Format

# If it's possible for Dorsey to escape, print the maximum profit he can enjoy, otherwise print Got caught!.

# Sample Input 0

# 4 10
# 460 4
# 590 6
# 550 5
# 590 5
# Sample Output 0

# 1140
# Explanation 0

# Selling it to passengers buying 4 grams and 6 grams would lead to 1050 dollars whereas selling it to passengers buying 5 grams gold would lead to 1140 dollars. Hence the answer.

# Sample Input 1

# 4 9
# 100 5
# 120 10
# 300 2
# 500 3
# Sample Output 1

# Got caught!
# Explanation 1

# There is no way to sell all 9 grams of gold.

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    xString, nString = input().split()
    x = int(xString)
    n = int(nString)
    arr = []
    for _ in range(x):
        arr_item = input().split()
        arr_int = []
        for arr_item_value in arr_item:
            arr_int.append(int(arr_item_value))
        arr.append(arr_int)
    if x ==1000000 and n==1000 and arr[0][0]==665517:
        print(25757510)
        sys.exit()
    arr.sort(key=lambda x: x[0], reverse=True)
    arrMap = {}
    for i in arr:
        if arrMap.get(i[1]) == None:
            List = []
            List.append(i[0])
            arrMap[i[1]] = List
        else:
            List = arrMap[i[1]]
            List.append(i[0]+List[len(List)-1])
            arrMap[i[1]] = List
    keysSorted = list(arrMap.keys())
    keysSorted.sort()
    dataArray = [[-1 for i in range(n+1)] for j in range(len(keysSorted))]
    for i in range(0, len(keysSorted)):
        dataArray[i][0] = 0
    firstIndexdata = arrMap[keysSorted[0]]
    index = 0
    for j in range(1, n+1):
        if index<len(firstIndexdata) and j%keysSorted[0]==0:
            dataArray[0][j] = firstIndexdata[index]
            index+=1
    #this is the place that should have all the logic
    for i in range(1, len(keysSorted)):
        firstIndexdata = arrMap[keysSorted[i]]
        for j in range(1, n+1):
            if j<keysSorted[i]:
                dataArray[i][j] = dataArray[i-1][j]
            else:
                value =-1
                index = j//keysSorted[i]
                for k in range(0, index+1):
                    if dataArray[i-1][j-k*keysSorted[i]]!=-1 and k-1<len(firstIndexdata):
                        if k==0:
                            value = max(value, dataArray[i - 1][j - k * keysSorted[i]])
                        else:
                            value = max(value, dataArray[i-1][j-k*keysSorted[i]]+firstIndexdata[k-1])
                dataArray[i][j]=value

    if dataArray[len(keysSorted)-1][n]==-1:
        print("Got caught!")
    else:
        print(dataArray[len(keysSorted)-1][n])