## 35. Search Insert Position

**Runtine-4ms Beats-3.13%**

**Memory- 12.93MB Beats-61.09%**

---
## SOLUTION:

```PYTHON
class Solution(object):

    def searchInsert(self, nums, target):

        """

        :type nums: List[int]

        :type target: int

        :rtype: int

        """

        top, low = len(nums)-1, 0

        while top>=low:

            middle = (top+low)/2

            if nums[middle]== target:

                return target

            elif nums[middle]< target:

                low = middle+1

            elif nums[middle]> target:

                high = middle-1

        if nums[0]>target:

            return 0

        elif nums[len(nums)-1]<target:

            return len(nums)-1

        else:

            return low
```
