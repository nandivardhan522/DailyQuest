class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

'''
Time Complexity:
    Traversal:Each node is visited exactly once during the rearrangement process.
    Time complexity: O(n), where n is the number of nodes in the list.
Space Complexity:
    No additional data structures are used; 
    only a constant amount of extra space is needed for pointers (odd, even, even_head).
    Space complexity: O(1).
'''