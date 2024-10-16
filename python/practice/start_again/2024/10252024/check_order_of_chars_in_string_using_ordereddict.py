#   https://www.geeksforgeeks.org/using-ordereddict-python-check-order-characters-string/

def checkOrder(string, pattern):
    i, j = 0, 0 
    for char in string:
        if char == pattern[j]:
            j += 1
        if j == len(pattern):
            return True
        i +=1
    return False

if __name__ == "__main__":
    string = 'engineers rock'
    pattern = 'er'
    print (checkOrder(string, pattern))