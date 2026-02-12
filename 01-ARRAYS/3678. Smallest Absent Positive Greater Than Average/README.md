## 3678. Smallest Absent Positive Greater Than Average

**Runtime- 3ms  83.33%**

**Memory 12.35mb  90.91%**
---

## SOLUTIONS
```PYTHON
class Solution(object):

    def smallestAbsent(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        leng = len(nums)

        if leng ==1:

            return nums[0]+1 if nums[0]+1 >0 else 1

        avg = (sum(nums))/float(leng)

        i = avg

        if float(i) != int(i):

            i = int(avg)+1

        else:

            i = int(avg)+1

        while i in nums:

            i+=1

        if i<=0:

            j =1

            while j in nums:

                j+=1

            return j

        else:

            return i
```
