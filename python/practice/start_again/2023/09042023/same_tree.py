# 100. Same Tree
# Easy
# 10.3K
# 198
# Companies
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false

def isSameTree(p,q):
    if p == None and q == None: # Same Tree
        return True
    if p == None or q == None: # Different Size
        return False
    if p.val != q.val: # Different Nodes
        return False
    return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)



if __name__ == "__main__":
    p = [1,2,1]
    q = [1,1,2]
    print ("{}".format(isSameTree(p,q)))