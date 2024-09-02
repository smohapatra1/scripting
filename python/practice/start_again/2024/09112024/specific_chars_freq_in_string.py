#   https://www.geeksforgeeks.org/python-specific-characters-frequency-in-string-list/

# Use dictionary 
# Loop through the chars
# Use counter with index
# Return Dictionary

def CharFreq(test_list, chr_list):
    d = dict()
    for i in chr_list:
        d[i] = test_list[0].count(i)
    return d
if __name__ == "__main__":
    test_list = ["geeksforgeeks is best for geeks"]
    chr_list = ['e', 'b', 'g']
    result = CharFreq(test_list, chr_list)
    print (result)