#   You can see two unsorted arrays. How will you find all pairs whose sum is x?
#   https://www.google.com/search?client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNS-n1aK1uRUJ-SJ-xG3jhDR-PIaQ:1751740901194&q=You+can+see+two+unsorted+arrays.+How+will+you+find+all+pairs+whose+sum+is+x?+program+in+python%C2%A0&spell=1&sa=X&ved=2ahUKEwjp0p2xr6aOAxVdhIkEHVFiAR4QBSgAegQIExAB&biw=1729&bih=876&dpr=2
def found_pairs_sum(arr1, arr2, x):
    found_pairs = []
    set_arr2 = set(arr2)
    for num1 in arr1:
        component = x - num1
        if component in set_arr2:
            found_pairs.append((num1, component))
    return found_pairs
arr1 = [ 1, 2, 3, 7, 5, 4]
arr2 = [ 0, 7, 4, 3, 2, 1]
target_sum = 8 
pairs = found_pairs_sum(arr1, arr2, target_sum)
print (f"Target pairs are {target_sum}: {pairs}") 
