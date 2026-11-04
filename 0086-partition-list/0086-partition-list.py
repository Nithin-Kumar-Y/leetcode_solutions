# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy= ListNode(0)
        dummy.next = head
        prev=dummy
        target=dummy # previous node of the targeted place
        temp=target.next
        while temp and temp.val<x:
            temp=temp.next
            target=target.next
        curr=prev.next
        found =False
        while curr:
            if curr.val<x:
                if found==False:
                    prev=curr
                    curr=curr.next
                else:
                    nxt = curr.next

                    curr.next = target.next
                    target.next=curr
                    prev.next=nxt

                    target=curr
                    curr=nxt
            else:
                found=True
                prev=curr
                curr=curr.next
        return dummy.next