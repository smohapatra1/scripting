# #   https://leetcode.com/problems/all-possible-full-binary-trees/
# 894. All Possible Full Binary Trees
# Medium
# 4.9K
# 328
# Companies
# Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

# A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

# Example 1:


# Input: n = 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Example 2:

# Input: n = 3
# Output: [[0,0,0]]

def AllpossibleFBT( n: int ) -> TreeNode:
    if n % 2 == 0:
        return []
    res = 0 
    def _AllpossibleFBT(n):
        if n in res:
            return res(n)
        list = []
        if n==1:
            list.append(TreeNode, 0)
        else:
            for i in range(1, n, -2, 2 ):
                lTrees=__AllpossibleFBT(i)
                rTrees=_AllpossibleFBT(n-i-1)
                for lt in lTrees:
                    for rt in rTrees:
                        list.append(TreeNode(0, lt, rt))

        res[n]= list
        return list


if __name__ == "__main__":
    n=8
    print ("{}".format(AllpossibleFBT(n)))