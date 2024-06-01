# #   https://www.hackerrank.com/challenges/real-estate-broker/problem?isFullScreen=true

# You are a real estate broker in ancient Knossos. You have  unsold houses, and each house  has an area, , and a minimum price, . You also have  clients, and each client  wants a house with an area greater than  and a price less than or equal to .

# Each client can buy at most one house, and each house can have at most one owner. What is the maximum number of houses you can sell?

# Input Format

# The first line contains two space-separated integers describing the respective values of  (the number of clients) and  (the number of houses).
# Each line  of the  subsequent lines contains two space-separated integers describing the respective values of  and  for client .
# Each line  of the  subsequent lines contains two space-separated integers describing the respective values of  and  for house .

# Constraints

# , where .
# , where .
# Output Format

# Print a single integer denoting the maximum number of houses you can sell.

# Sample Input 0

# 3 3
# 5 110
# 9 500
# 20 400
# 10 100
# 2 200
# 30 300
# Sample Output 0

# 2
# Explanation 0

# Recall that each client  is only interested in some house  where  and . The diagram below depicts which clients will be interested in which houses:

# image

# Client  will be interested in house  because it has more than  units of space and costs less than . Both of the other houses are outside of this client's price range.
# Client  will be interested in houses  and , as both these houses have more than  units of space and cost less than . They will not be interested in the remaining house because it's too small.
# Client  will be interested in house  because it has more than  units of space and costs less than . They will not be interested in the other two houses because they are too small.
# All three clients are interested in the same two houses, so you can sell at most two houses in the following scenarios:

# Client  buys house  and client  buys house .
# Client  buys house  and client  buys house .
# Client  buys house  and client  buys house .
# Thus, we print the maximum number of houses you can sell, , on a new line.


#!/bin/python3

import os
import sys

#
# Complete the realEstateBroker function below.
#

n, m = map(int, input().split())
buy, house = [], []
for i in range(n):
    buy.append(tuple(map(int, input().split())))
for i in range(m):
    house.append(tuple(map(int, input().split())))
buy.sort(key=lambda x: x[1])
house.sort()
sold = [False for i in range(n)]
a = 0
for h in range(m):
    for c in range(n):
        if not sold[c]:
            if buy[c][0] <= house[h][0] and buy[c][1] >= house[h][1]:
                sold[c] = True
                a += 1
                break
print(a)

# def realEstateBroker(clients, houses):
#     #
#     # Write your code here.
#     #

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nm = input().split()

#     n = int(nm[0])

#     m = int(nm[1])

#     clients = []

#     for _ in range(n):
#         clients.append(list(map(int, input().rstrip().split())))

#     houses = []

#     for _ in range(m):
#         houses.append(list(map(int, input().rstrip().split())))

#     result = realEstateBroker(clents, houses)

#     fptr.write(str(result) + '\n')

#     fptr.close()
