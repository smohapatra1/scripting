#   Write a Code To Find the Maximum Depth of a Binary Tree.


def maxDepth(root):
    def dfs(root, depth):
        if not root:
            return depth
        return (max(dfs(root.left, depth+1) , dfs(root.right, depth+ 1)))
    return dfs(root, 0)


if __name__ == "__main__":
    root = [3,9,20,15,7]
    print ("Max Depth is {}".format(maxDepth(root)))