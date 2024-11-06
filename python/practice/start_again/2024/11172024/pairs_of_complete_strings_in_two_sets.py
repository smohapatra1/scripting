#   https://www.geeksforgeeks.org/python-set-pairs-complete-strings-two-sets/

def completePair(set1, set2):
    count = 0 
    for str1 in set1:
        for str2 in set2:
            result = str1 + str2
            temp = set([char for char in result if ord(char) >= ord('a') and ord(char) <= ord('z')])
            if len(temp) == 26:
                count = count + 1
                print (result)
    return count 

if __name__ == "__main__":
    set1 = ['abcdefgh', 'geeksforgeeks','lmnopqrst', 'abc'] 
    set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz','defghijklmnopqrstuvwxyz'] 
    print ("Count is : ", completePair(set1, set2))