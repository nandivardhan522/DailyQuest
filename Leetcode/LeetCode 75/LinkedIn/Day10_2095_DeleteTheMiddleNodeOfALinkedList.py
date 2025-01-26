class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head

'''
Complexity Analysis
    Time Complexity:
        Two-Pointer Version: Traverses the list once to find the middle node, making it O(n).
Space Complexity:
    O(1), as we only used pointers and no additional data structures.

'''