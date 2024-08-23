#       https://www.geeksforgeeks.org/python-extract-words-starting-with-k-in-string-list/

#   Loop through the elements
#   Remove the spaces and split the words 
#   Compare the splitted works with the required value with starting element 
#   If found then append the splitted works 
#   Return the splitted words 

def Extract(test_list, k ):
    # Solution 1 
    # res = []
    # for ele in test_list:
    #     temp = ele.split()
    #     for ele2 in temp:
    #         if ele2[0].lower() == k.lower():
    #             res.append(ele2)
    # return res
    # Solution 2 
    res = [ ele for temp in test_list for ele in temp.split() if ele[0].lower() == k.lower()]
    return res

if __name__ == "__main__":
    test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]
    k = 'g'
    result = Extract(test_list, k )
    print (result)