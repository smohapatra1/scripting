#   https://www.geeksforgeeks.org/deletion-in-hash-tables-using-python/


hash = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
print ("Original Hash List", hash)
delete_key = 'B'
if delete_key in hash:
    del hash[delete_key]
    print ("Key '{}' deleted from hash table ".format(delete_key))
else:
    print ("Key '{}' is not found in hash table".format(delete_key))
print ("Updated Hash List", hash)