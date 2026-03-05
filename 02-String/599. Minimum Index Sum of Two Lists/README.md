## 599. Minimum Index Sum of Two Lists


**Runtime  -8ms  Beats- 69.31%**


**Memory- 12.55MB   - Beats- 95.31%**

---
## SOLUTION
```PYTHON

class Solution(object):

    def findRestaurant(self, list1, list2):

        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        roll = { j:indx for indx,j in enumerate(list1)}
 
        ans = []
        best =float('inf')
        for indx, ch in enumerate(list2):
            if ch in roll:
                s = indx+ roll[ch]
                if s< best:
                    ans = [ch]
                    best = s
                elif s== best:
                    ans.append(ch)
                
        return ans
```
