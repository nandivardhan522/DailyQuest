from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root) -> int:
        self.maxi=0
        self.d=defaultdict(list)
        self.dfs(root)
        return self.maxi
    def dfs(self,node):
        if(not node):
            return None
        self.dfs(node.left)
        self.dfs(node.right)
        self.test(node)
    def test(self,temp):
        if(not temp.left):
            self.d[temp].append(0)
        else:
            self.d[temp].append(self.d[temp.left][1]+1)
        if(not temp.right):
            self.d[temp].append(0)
        else:
            self.d[temp].append(self.d[temp.right][0]+1)
        if(max(self.d[temp])>self.maxi):
            self.maxi=max(self.d[temp])

'''
Time Complexity Analysis
Let's analyze the time complexity step by step:

Depth-First Search (DFS) Traversal
The dfs function traverses every node exactly once.
There are N nodes in the tree, so the traversal takes O(N) time.
Processing Each Node (test function)
Each node's left and right child values are accessed in the dictionary (self.d), which takes O(1).
Each node performs a constant number of operations, so this also takes O(1) per node.
Since both DFS traversal and processing each node take O(N) + O(N) = O(N), the overall time complexity is O(N).

Space Complexity Analysis
Recursive Call Stack
The dfs function uses recursion, and in the worst case (a skewed tree), the recursion depth could be O(N).
In a balanced tree, the recursion depth is O(log N).
Dictionary Storage (self.d)
The dictionary stores at most N nodes, each with an array of size 2.
This results in O(N) space usage.
Thus, in the worst case, the space complexity is O(N) (both recursion stack and dictionary storage).
'''