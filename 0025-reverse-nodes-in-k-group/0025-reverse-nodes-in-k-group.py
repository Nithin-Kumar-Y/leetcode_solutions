# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        dummy= ListNode(0)
        dummy.next = head
        prev_last=dummy
        while True:
            curr_last=prev_last
            for _ in range(k):
                curr_last = curr_last.next
                if not curr_last:
                    return dummy.next
            next_first = curr_last.next
            first=prev_last.next
            prev=prev_last
            curr=first
            while curr != next_first:
                nxt = curr.next
                curr.next = prev
                prev=curr
                curr=nxt
            prev_last.next= prev
            first.next = next_first
            if not prev_last.next:
                return dummy.next
            prev_last=first
            first=prev_last.next
        return dummy.next