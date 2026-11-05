# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        prev=None
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        
        second = slow.next
        slow.next = None
        curr= second
        prev=None
        while curr:
            nxt = curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        second = prev
        a= head
        b=second
        while a and b:
            a_nxt= a.next
            b_nxt = b.next
            b.next=a.next
            a.next=b
            b=b_nxt
            a=a_nxt