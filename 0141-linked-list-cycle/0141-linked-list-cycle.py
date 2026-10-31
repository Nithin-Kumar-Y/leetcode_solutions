# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        slow = dummy
        while fast.next != None and fast.next.next != None:
            fast=fast.next.next
            slow = slow.next
            if fast ==slow:
                return True
        return False