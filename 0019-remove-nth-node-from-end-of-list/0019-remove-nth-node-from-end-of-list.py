# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head or n<1:
            return head
        total = 0
        temp = head
        while temp != None:
            temp= temp.next
            total+=1
        if total==n:
            return head.next
        temp = head
        for i in range(total-n-1):
            temp= temp.next
        temp.next = temp.next.next
        return head