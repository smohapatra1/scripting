# #https://leetcode.com/problems/operations-on-tree/
# 1993. Operations on Tree
# Medium
# 427
# 70
# Companies
# You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of the ith node. The root of the tree is node 0, so parent[0] = -1 since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

# The data structure should support the following functions:

# Lock: Locks the given node for the given user and prevents other users from locking the same node. You may only lock a node using this function if the node is unlocked.
# Unlock: Unlocks the given node for the given user. You may only unlock a node using this function if it is currently locked by the same user.
# Upgrade: Locks the given node for the given user and unlocks all of its descendants regardless of who locked it. You may only upgrade a node if all 3 conditions are true:
# The node is unlocked,
# It has at least one locked descendant (by any user), and
# It does not have any locked ancestors.
# Implement the LockingTree class:

# LockingTree(int[] parent) initializes the data structure with the parent array.
# lock(int num, int user) returns true if it is possible for the user with id user to lock the node num, or false otherwise. If it is possible, the node num will become locked by the user with id user.
# unlock(int num, int user) returns true if it is possible for the user with id user to unlock the node num, or false otherwise. If it is possible, the node num will become unlocked.
# upgrade(int num, int user) returns true if it is possible for the user with id user to upgrade the node num, or false otherwise. If it is possible, the node num will be upgraded.
 

# Example 1:


# Input
# ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
# [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
# Output
# [null, true, false, true, true, true, false]

# Explanation
# LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
# lockingTree.lock(2, 2);    // return true because node 2 is unlocked.
#                            // Node 2 will now be locked by user 2.
# lockingTree.unlock(2, 3);  // return false because user 3 cannot unlock a node locked by user 2.
# lockingTree.unlock(2, 2);  // return true because node 2 was previously locked by user 2.
#                            // Node 2 will now be unlocked.
# lockingTree.lock(4, 5);    // return true because node 4 is unlocked.
#                            // Node 4 will now be locked by user 5.
# lockingTree.upgrade(0, 1); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
#                            // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
# lockingTree.lock(0, 1);    // return false because node 0 is already locked.
 
from typing import List
class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent=parent
        self.tree=[[] _ in parent]
        for i, x in enumerate(parent):
            if x !=-1 : self.tree[x].append(i)
        self.locked = {}
        

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        self.locked[num] == user
        return True
        

    def unlock(self, num: int, user: int) -> bool:
        if self.locked.get(num) != user:
            return False
        self.locked. pop(num)
        return True
        

    def upgrade(self, num: int, user: int) -> bool:
        if num is self.locked:
            return False
        node = num
        while node != -1 :
            if node in self.locked: break 
            node= self.parent[node]
        else:
            stack = [num]
            descendant = []
            while stack:
                node=stack.pop()
                if node in self.locked: descendant.append(node)
                for child in self.tree[node]: stack.append(child)
            if descendant:
                self.locked[num] = user 
                for node in descendant: self.locked.pop(node)
                return True
        return False    


        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)