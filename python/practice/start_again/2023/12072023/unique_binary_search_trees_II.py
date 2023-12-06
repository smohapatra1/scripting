# #   https://leetcode.com/problems/unique-binary-search-trees-ii/

# 95. Unique Binary Search Trees II
# Medium
# 7.4K
# 489
# Companies
# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

# Example 1:


# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

class TreeNode:
    def __init__(self, val: int, next=None, left=None):
        self.val = val
        self.left=left
        self.next=next

def UniqueTrees( n: int )-> TreeNode:
    if n == 0:
        return []
    res = {}
    def generate_trees( start, end ):
        if (start, end) in res :
            return res[(start, end)]
        trees = []
        if start > end:
            trees.append(None)
            return trees
        for root_val in range(start, end +1):
            left_trees=generate_trees(start, root_val - 1)
            right_trees = generate_trees(root_val + 1, end)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root=TreeNode(root_val, left_tree, right_tree)
                    trees.append(root)
        res[(start, end)] = trees
        return trees
    return generate_trees(1, n)



if __name__ == "__main__":
    n=3
    print ("{}".format(UniqueTrees(n)))
