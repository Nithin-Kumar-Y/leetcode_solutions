## 219. Contains Duplicate II

**Runtime- 58ms  Beats- 18.56%**


**Memory- 23.93MB  Beats- 79.24%**

---
## SOLUTION
```PYTHON
class Solution(object):

    def containsNearbyDuplicate(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        from collections import Counter

        c = Counter()
        for indx, ch in enumerate(nums):
            if ch in c:
                if abs(c[ch]-indx) <=k:
                    return True
            c[ch] = indx

        return False
```
