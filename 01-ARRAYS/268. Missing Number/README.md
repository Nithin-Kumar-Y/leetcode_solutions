## 268. Missing Number

**RUNTIME 9MS 34.82%**

**SPACCE  14.03MB  5.23%**
---
## SOLUTIONS
```PYTHON

class Solution(object):

    def missingNumber(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        nums = set(nums)

        for i in range(len(nums)+1):

            if i not in nums:

                return i
```
