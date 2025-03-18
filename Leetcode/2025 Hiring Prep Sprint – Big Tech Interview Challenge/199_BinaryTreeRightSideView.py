from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        queue = deque([])
        queue.append((root,0))
        d={}
        while queue:
            node, level = queue.popleft()
            if node is not None:
                d[level] = node.val
                if(node.left is not None):
                    queue.append((node.left,level+1))
                if node.right is not None:
                    queue.append((node.right,level+1))
        res = list(d.values())
        return res

root = [1,2,3,None,5,None,4]
'''
'''
