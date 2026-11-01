# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a=headA
        b=headB
        curr=0
        while a and b:
            if a==b:
                return a
            a=a.next
            b=b.next
            if not a:
                a=headB
                curr+=1
                if curr>2:
                    return None
            if not b:
                b=headA
                curr+=1
                if curr>2:
                    return None
        return None