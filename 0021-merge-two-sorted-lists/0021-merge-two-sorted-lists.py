# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        a = list1
        b=list2
        head = ListNode(-1)
        newList = head
        while a and b:
            if a.val<=b.val:
                newList.next = ListNode(a.val)
                newList = newList.next
                a=a.next
            else:
                newList.next = ListNode(b.val)
                newList = newList.next
                b= b.next
        if a:
            newList.next = a
        else:
            newList.next = b
        return head.next