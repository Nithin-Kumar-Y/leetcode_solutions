##  3795. Minimum Subarray Length With Distinct Sum At Least K

**Runtime- 769ms  Beats  34.67%**


**Memory 25.04MB Beats- 94.67%**

---
## SOLUTIONS
```PYTHON

class Solution(object):

    def minLength(self, nums, k):

        from collections import defaultdict

        count = defaultdict(int)
        total = 0
        l = 0
        best = float('inf')

        for r in range(len(nums)):

            val = nums[r]
            count[val] += 1

            if count[val] ==1:
                total += val

            while total >= k:
                best = min(best, r - l + 1)
                count[nums[l]] -= 1

                if count[nums[l]]==0:
                    del count[nums[l]]
                    total -= nums[l]
                l += 1

        return best if best != float('inf') else -1
```
