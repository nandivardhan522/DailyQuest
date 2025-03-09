class Solution:
    # One step right and then always left
    def successor(self, root) -> int:
        root = root.right
        while root.left:
            root = root.left
        return root.val

    # One step left and then always right
    def predecessor(self, root) -> int:
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root, key: int):
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # The node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root

'''
Time Complexity:
Worst Case: O(n)
Best/Average Case: O(log n)
Space Complexity:
Worst Case: O(n)
Best/Average Case: O(log n)
'''