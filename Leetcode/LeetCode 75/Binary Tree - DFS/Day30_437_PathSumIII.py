# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        self.numOfPaths=0
        self.dfs(root,targetSum)
        return self.numOfPaths
    def dfs(self, node, target):
        if(not node):
            return None
        self.dfs(node.left, target)
        self.test(node,target)
        self.dfs(node.right, target)
    def test(self, node, target):
        if(not node):
            return
        if(node.val==target):
            self.numOfPaths+=1
        self.test(node.left,target-node.val)
        self.test(node.right,target-node.val)


'''
Time Complexity:
Worst case (skewed tree): O(n²)
Best case (balanced tree): O(n \log n)
Space Complexity:
Worst case (skewed tree): O(n)
Best case (balanced tree): O(\log n)
'''