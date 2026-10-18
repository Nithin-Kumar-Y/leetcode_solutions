# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        temp = head
        odd = ListNode(temp.val)
        odd.next = None
        even = ListNode(0)
        even.next = None
        curr = 2
        t1= odd
        t2= even
        temp = temp.next
        while temp:
            newNode = ListNode(temp.val)
            if curr%2==1:
                t1.next = newNode
                t1=t1.next
            else:
                t2.next= newNode
                t2= t2.next
            curr+=1
            temp = temp.next
        t1.next= even.next
        return odd