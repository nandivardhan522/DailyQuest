# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if(not root):
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return max(left,right)+1

'''
Complexity Analysis:
Time Complexity:
The function visits each node exactly once.
If the tree has N nodes, the time complexity is O(N).
Space Complexity:
Best case (Balanced Tree): O(log N) (Height of tree, due to recursion stack).
Worst case (Skewed Tree): O(N) (If the tree is a linked list, recursion depth is N).
'''