## 876. Middle of the Linked List

**Runtime- 0ms- 100%**

**Space- 12.40mb 89.02%**
---

## SOLUTION
```PYTHON

# Definition for singly-linked list.

# class ListNode(object):

#     def __init__(self, val=0, next=None):

#         self.val = val

#         self.next = next

class Solution(object):

    def middleNode(self, head):

        """

        :type head: Optional[ListNode]

        :rtype: Optional[ListNode]

        """

        temp = head

        count = 0

        while temp.next != None:

            temp = temp.next

            count+=1

        if count%2 !=0:

            turn = (count+1)//2

        else:

            turn = count//2

        curr = head

        for i in range(turn):

            curr = curr.next

        return curr
```
