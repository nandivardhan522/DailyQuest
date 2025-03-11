# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        node=None
        while(head):
            temp=head
            head=head.next
            temp.next=node
            node=temp
        return node
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''