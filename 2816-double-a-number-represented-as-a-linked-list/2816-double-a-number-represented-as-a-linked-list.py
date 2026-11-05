# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry=0
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        temp = prev
        while temp:
            x = temp.val *2+ carry
            temp.val= x%10
            carry= x//10
            if not temp.next:
                break
            temp=temp.next
        if carry:
            temp.next = ListNode(carry)
        head= None
        curr=prev
        while curr:
            nxt = curr.next
            curr.next=head
            head=curr
            curr=nxt
        return head