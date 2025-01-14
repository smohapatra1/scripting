#   https://www.geeksforgeeks.org/python-program-for-linear-search/

import re

def LinearSearchUsingRegex(my_list, pattern):
    regex = re.compile(pattern)
    for index, ele in enumerate(my_list):
        if regex.search(ele):
            return f"Pattern found in element '{ele}' at index '{index}'"
    return "Pattern not found in the list" 

if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]
    pattern = "an"
    print (LinearSearchUsingRegex(my_list, pattern))