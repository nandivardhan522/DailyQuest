# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        temp=head
        length=0
        while(temp):
            length+=1
            temp=temp.next
        c=length//2
        temp=head
        head2=None
        i=0
        while(i<c-1):
            temp=temp.next
            i+=1
        head2=temp.next
        temp.next=None
        maxi=0
        tail=None
        while(head2):
            temp=head2
            head2=head2.next
            temp.next=tail
            tail=temp
        for i in range(c):
            maxi=max(maxi,head.val+tail.val)
            head=head.next
            tail=tail.next
        return maxi
'''
Time Complexity: The final time complexity is O(N).
Space Complexity: The final space complexity is O(1).
'''