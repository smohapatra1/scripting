'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
class Solution:
    def k_list(self, lists):
        res =[]
        for i in range(len(k_list)) :
            item=lists[i]
            while item != None:
                res.append(item.val)
                item = item.next
            res = sorted(res)
            return res

#k_list(input("Enter lists with space: "),input("Enter lists with space: "), input("Enter lists with space: ")) 
lists(input("Enter lists with space: ")) 
