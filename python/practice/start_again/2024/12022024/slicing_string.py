# #   https://www.geeksforgeeks.org/problems/slicing-in-string-python/1

# Now, lets look into this through a question. Given a string of braces named bound_by, and a string named tag_name. The task is to print a new string such that tag_name is in the middle of bound_by.

# Input: 
# bound_by = [[]], tag_name = tag
# Output:
# [[tag]]
def Slicing(bound_by, tag_name):
    return bound_by[0:len(bound_by)//2] + tag_name + bound_by[len(bound_by)//2:]

if __name__ == "__main__":
    bound_by = [[]]
    tag_name = "tag"
    print (Slicing(bound_by, tag_name))
