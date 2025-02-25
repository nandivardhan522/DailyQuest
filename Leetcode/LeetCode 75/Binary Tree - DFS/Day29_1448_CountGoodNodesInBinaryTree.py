# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root) -> int:
        queue=[]
        queue.append([root,root.val])
        c=1
        while(len(queue)>0):
            try:
                queue.append([queue[0][0].left,max(queue[0][0].left.val,queue[0][1])])
                if(queue[0][1]<=queue[0][0].left.val):
                    c+=1
            except:
                pass
            try:
                queue.append([queue[0][0].right,max(queue[0][0].right.val,queue[0][1])])
                if(queue[0][1]<=queue[0][0].right.val):
                    c+=1
            except:
                pass
            queue.pop(0)
        return c

'''
Time Complexity Analysis
The function uses Breadth-First Search (BFS) via a queue to traverse the tree.
Each node is processed once, meaning:
It is dequeued once.
At most two child nodes (left and right) are enqueued per node.
The operations inside the loop (checking values, updating c, and appending to the queue) take constant time O(1).
Thus, for a tree with N nodes, the function runs in:O(N)

Space Complexity Analysis
The space required is primarily due to:
Queue Storage:
In the worst case (a full binary tree), the queue stores up to one level of nodes at a time.
The maximum number of nodes in a level of a balanced binary tree is N/2 (at the last level).
This gives a worst-case space complexity of O(N) in the case of a skewed tree and O(N/2) = O(N) in the case of a balanced tree.
Additional Variables:c (integer counter) → 
O(1)
Temporary storage for node values → O(1)
Thus, the worst-case space complexity is: O(N)
'''