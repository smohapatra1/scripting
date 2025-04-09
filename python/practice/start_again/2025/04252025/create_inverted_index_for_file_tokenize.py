#   https://www.geeksforgeeks.org/create-inverted-index-for-file-using-python/

def words(file):
    result = []
    for i in range(len(file)):
        token = []
        token = file[i].split()
        result.append(token)
    return result