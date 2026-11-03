# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a =l1
        b=l2
        newList = ListNode(-1)
        carry=0
        temp = newList
        while a or b or carry:
            x = a.val if a else 0
            y= b.val if b else 0
            t = x+y+carry
            temp.next = ListNode(t%10)
            carry=t//10
            temp=temp.next
            if a:
                a=a.next
            if b:
                b=b.next
        return newList.next