## 228. Summary Ranges

**Runtime- 0ms Beats-100.00%**

**Memory- 12.57MB Beats-19.23%**

---
## SOLUTION
```PYTHON

class Solution(object):

    def summaryRanges(self, nums):

        """

        :type nums: List[int]

        :rtype: List[str]

        """

        if not nums:

            return nums

        first, last = None, 0

        ans = []

        first =last = nums[0]

        for i in range(1, len(nums)):

            if last+1 == nums[i]:

                last = nums[i]

            else:

                if last != first:

                    ans.append(str(first) +"->"+ str(last))

                else:

                    ans.append(str(last))

                first=last = nums[i]

        if last == first:

            ans.append(str(last))

        else:

            ans.append(str(first)+"->"+str(last))

        return ans
```
