## 206. REVERSE THE LINKED LIST

**Time- 0ms, 100%**

**Space- 14.36mb 78.18%**

---
## SOLUTION
```PYTHON

Definition for singly-linked list.

class ListNode(object):

    def __init__(self, val=0, next=None):

        self.val = val

         self.next = next

class Solution(object):

    def reverseList(self, head):

        """

        :type head: Optional[ListNode]

        :rtype: Optional[ListNode]

        """

        prev = None

        curr = head

        while curr != None:

            nxt = curr.next

            curr.next = prev

            prev = curr

            curr = nxt

        return prev
```
