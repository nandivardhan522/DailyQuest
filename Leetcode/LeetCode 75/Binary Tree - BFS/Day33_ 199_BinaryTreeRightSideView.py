# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return []
        queue=[]
        queue.append(root)
        temp=[]
        i=0
        ele=[root.val]
        while(i<len(queue)):
            print(queue[i])
            if(queue[i].left!=None):
                temp.append(queue[i].left)
            if(queue[i].right!=None):
                temp.append(queue[i].right)
            i+=1
            if(i>=len(queue)):
                i=0
                if(len(temp)==0):
                    return ele
                ele.append(temp[-1].val)
                queue=temp.copy()
                temp=[]