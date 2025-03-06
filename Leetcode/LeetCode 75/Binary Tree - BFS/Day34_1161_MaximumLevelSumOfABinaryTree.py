from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root) -> int:
        d=defaultdict(int)
        l=[]
        def dfs(node,level):
            if not node:
                return node
            if(len(l)==level):
                l.append(node.val)
            else:
                l[level]+=node.val
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return l.index(max(l))+1
'''

Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(N), where N is the number of nodes in the tree

1 (due to the recursive call stack and the list of level sums).
'''