## 56. Merge Intervals

**RUNTIME- 16MS  13.36%**

**SPACE- 17.04MB  30.42%**
---
## SOLUTIONS
```PYTHON
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = []
        left, right = None, None
        for i in intervals:
            if i[0]>right:
                ans.append([left, right])
                left,right = i[0],i[-1]
            else:
                right = max(right, i[-1])
        ans.append([left, right])
        return ans[1:]
```
