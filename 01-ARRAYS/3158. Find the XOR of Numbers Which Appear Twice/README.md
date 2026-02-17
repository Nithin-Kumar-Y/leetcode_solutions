## 3158. Find the XOR of Numbers Which Appear Twice


**RUNTIME = 0MS 100%**

**12.31MB  92.91%**


---
## SOLUTIONS
```PYTHON
class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        slow= 0
        ans = None
        for fast in range(1, len(nums)):
            if nums[slow]==nums[fast]:
                if ans is None:
                    ans = nums[slow]
                else:
                    ans = ans^nums[slow]
            slow+=1
        return 0 if ans is None else ans
```
