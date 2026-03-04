## 806. Number of Lines To Write String


**Runtime-  24ms   Beats- 13.11%**


**Memory- 12.52Mb    Beats- 29.51%**


---
# SOLUTIONS
```PYTHON

class Solution(object):
    def numberOfLines(self, widths, s):

        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """

        total = 0
        line =0
        for ch in s:
            value = (widths[ord(ch)-ord('a')])
            if total+ value> 100:
                total = value 
                line+=1
            else:
                total+=value
        if total !=  0:
            line+=1

        return [line, total]
```
