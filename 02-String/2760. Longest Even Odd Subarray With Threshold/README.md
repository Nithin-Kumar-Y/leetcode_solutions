## 2760. Longest Even Odd Subarray With Threshold

**Runtime- 52ms  Beats- 53.75%**


**Memory- 12.32MB  Beats- 90.00%**

---
## SOLUTION 
```PYTHON

class Solution(object):

    def longestAlternatingSubarray(self, nums, threshold):

        best = 0
        l = 0

        for r in range(len(nums)):

            if nums[r] > threshold:
                l = r + 1
                continue

            if r == l:
                if nums[r] % 2 == 0:
                    best = max(best, 1)
                else:
                    l += 1
            else:
                if nums[r] % 2 != nums[r-1] % 2:
                    best = max(best, r - l + 1)
                else:
                    if nums[r] % 2 == 0:
                        l = r
                        best = max(best, 1)
                    else:
                        l = r + 1

        return best
```
