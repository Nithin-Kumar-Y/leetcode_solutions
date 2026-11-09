# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        best = 0
        fast = head
        slow = head
        prev=None
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow=slow.next
        first = slow.next
        slow.next= None
        while first:
            nxt= first.next
            first.next=prev
            prev=first
            first=nxt
        fast=head
        while prev:
            c= prev.val+ fast.val
            if c>best:
                best=c
            prev=prev.next
            fast=fast.next
        return best