# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return None
        slow = head
        fast = head
        if fast.next==None:
            return None
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                break
        if fast != slow:
            return None
        slow = head
        while slow !=fast:
            slow=slow.next
            fast =fast.next
        return slow