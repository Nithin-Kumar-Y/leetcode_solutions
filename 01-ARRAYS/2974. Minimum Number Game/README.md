## 2974. Minimum Number Game

**Runtime- 3ms 57.94%**

**Space- 12.47mb  581.5%**
---
## SOLUTIONS 
```PYTHON
class Solution(object):

    def numberGame(self, nums):

        """

        :type nums: List[int]

        :rtype: List[int]

        """

        nums.sort()

        arr = []

        for i in range(len(nums)//2):

            temp = nums[i*2:(i+1)*2]

            arr.extend(temp[::-1])

        return arr
```
---
## IDEAL SOLUTION
```PYTHON
class Solution:
    def numberGame(self, v):
        n = len(v)
        v.sort()
        for i in range(0, n, 2):
            if i + 1 < n:
                v[i], v[i + 1] = v[i + 1], v[i]
        return v
```
