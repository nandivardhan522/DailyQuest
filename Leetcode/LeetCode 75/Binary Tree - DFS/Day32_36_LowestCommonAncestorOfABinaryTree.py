# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if(not node):
                return
            if(node==p or node ==q):
                return node
            left=dfs(node.left)
            right=dfs(node.right)
            if(left and right):
                return node
            return left if left else right
        return dfs(root)

'''
Time Complexity:
The function performs a Depth-First Search (DFS) traversal of the binary tree.
In the worst case, it visits each node once.
If the tree has N nodes, the time complexity is O(N).
Space Complexity:
The function uses recursive DFS, which takes up space in the call stack.
In the worst case (a skewed tree), the recursion depth is O(N), leading to O(N) space complexity.
In a balanced tree, the recursion depth is O(logN), so the space complexity is O(logN) in that case.
'''