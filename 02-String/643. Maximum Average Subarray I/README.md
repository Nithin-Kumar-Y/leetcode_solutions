## 643. Maximum Average Subarray I

**Runtime- 170ms  Beats- 8.20%**


**Memory- 18.56MB  Beats- 93.27%**

---
## SOLUTION
``` PYTHON

class Solution(object):

    def findMaxAverage(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        total = sum(nums[:k])
        avg = total/float(k)
        l=1
        while l+k-1 < len(nums):
            total += (nums[l+k-1] - nums[l-1])
            
            avg = max(total/float(k) , avg)
            l+=1

        return avg
```
