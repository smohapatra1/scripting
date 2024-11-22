#   https://www.geeksforgeeks.org/python-maximum-and-minimum-k-elements-in-tuple/

test_tup = (3, 7, 1, 18, 9)
k = 2 

res = []
test_tup = list(sorted(test_tup))
for idx, val in enumerate(test_tup):
    if idx < k or idx >=len(test_tup) -k :
        res.append(val)
res = tuple(res)
print("The extracted values : " + str(res))