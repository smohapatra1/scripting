# 572. Subtree of Another Tree
# Easy
# 7.7K
# 446
# Companies
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false


def isSubtree(root,subRoot):
    def traverse_tree(node):
        if not node:
            return None
        return f"'#',{node.val} {traverse_tree(node.left)} {traverse_tree(node.right)}"
    return traverse_tree(subRoot) in traverse_tree(root)


if __name__ == "__main__":
    root = [3,4,5,1,2]
    subRoot = [4,1,2]
    print ("{}".format(isSubtree(root, subRoot)))