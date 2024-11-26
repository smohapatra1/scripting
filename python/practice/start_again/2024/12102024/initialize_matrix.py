#   https://www.geeksforgeeks.org/initialize-resrix-in-python/

rows = 3 
cols = 2 
res = [[ 0 for _ in range(cols)]] * rows 
print (f' Matrix with dimension {rows} * {cols} is {res}')
res[0][0], res[0][1] = 1,2
res[1][0], res[1][1] = 3,4
res[2][0], res[2][1] = 5,6
print(f'modified Matrix is {res}')

print(f'addr(res[0][0]) = {id(res[0][0])}, addr(res[0][1]) = {id(res[0][1])}')
print(f'addr(res[1][0]) = {id(res[1][0])}, addr(res[1][1]) = {id(res[1][1])}')
print(f'addr(res[2][0]) = {id(res[2][0])}, addr(res[2][1]) = {id(res[2][1])}')