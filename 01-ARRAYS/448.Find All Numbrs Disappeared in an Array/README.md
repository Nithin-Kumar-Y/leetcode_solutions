## 448. Find All Numbers Disappeared in an Array

**Runtime- 43ms Beats-42.81%**

**Memory-27.52MB Beats-43.91%**

---
## SOLUTION
```PYTHON
class Solution(object):

    def findDisappearedNumbers(self, nums):

        """

        :type nums: List[int]

        :rtype: List[int]

        """

        ans = set(i for i in range(1, len(nums)+1))

        for i in nums:

            ans.discard(i)

        return list(ans)
```
