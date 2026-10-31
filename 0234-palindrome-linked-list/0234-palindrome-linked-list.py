# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head.next:
            return True
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast != None:
            new_head = slow.next
        else:
            new_head = slow
        prev = None
        curr = new_head
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr=nxt
        temp = head
        while prev and temp:
            if temp.val != prev.val:
                return False
            temp=temp.next
            prev=prev.next
        return True