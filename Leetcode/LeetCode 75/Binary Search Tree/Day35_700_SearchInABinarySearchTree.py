# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val: int):
        if(not root):
            return
        if(root.val==val):
            return root
        if(val<root.val):
            return self.searchBST(root.left,val)
        elif(val>root.val):
            return self.searchBST(root.right,val)

'''
Time Complexity:
    Best Case: O(1)
    Average Case: O(log n)
    Worst Case: O(n)
Space Complexity:
    Average Case: O(log n)
    Worst Case: O(n)
'''