## 2089. Find Target Indices After Sorting Array

**RUNTIME- 3MS  37.67%**

**SPACE 12.64MB**
---
33 SOLUTIONS
```PYTHON
class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        nums.sort()
        i = 0
        while i < len(nums) and nums[i]<=target:
            if nums[i]== target:
                ans.append(i)
            elif nums[i]>target:
                break
            i+=1
        return ans
```
