# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        list1=[]
        def get_leaves(root):
            if(not root):
                return
            if(root.left == None and root.right == None ):
                list1.append(root.val)
            get_leaves(root.left)
            get_leaves(root.right)
        get_leaves(root1)
        k=list1.copy()
        list1=[]
        get_leaves(root2)
        if(len(k)!=len(list1)):
            return False
        return k == list1
'''

Complexity Analysis 
Time Complexity:

The helper function get_leaves(root) traverses the entire tree recursively.
Since each node is visited once, the traversal takes O(N1) for root1 (whereN1 is the number of nodes in tree1).
Similarly, it takes O(N2) for root2 (where N2 is the number of nodes in tree2).
Copying the list k = list1.copy() takes O(L1), where L1 is the number of leaf nodes in root1. In the worst case,
L1=O(N1).
The final comparison k == list1 takes O(L1) as well.
Thus, the overall time complexity is: O(N1+N2)
since extracting leaf sequences from both trees dominates the complexity.

Space Complexity:
The space used for storing the leaf values is O(L1 + L2), where L1 and L2 are the number of leaf nodes in root1 and root2, respectively.
The recursion stack in the worst case (for a skewed tree) takes O(H1 + H2), where
H1 andH2 are the heights of the trees.
In a balanced tree, the height is O(log N), while in a skewed tree, the height is O(N).
Thus, the worst-case space complexity is: O(N1+N2) when both trees are completely skewed.
'''