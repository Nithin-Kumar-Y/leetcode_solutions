## 3318. Find X-Sum of All K-Long Subarrays I

**Runtime-  60ms  Beats- 23.08%**


**Memory - 12.41MB  Beats- 69.23%**

---
## SOLUTION
```PYTHON
class Solution(object):

    def findXSum(self, nums, k, x):

        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        from collections import Counter

        ans= []
        for j in range(0, len(nums)-k+1):
            temp=0
            s = Counter(nums[j:j+k])
            if k==x:
                temp= sum(nums[j:j+k])
            else:
                c = sorted(s.items(), key=lambda v: (-v[1], -v[0]))[:x]
                
                for l in c:
                    temp+= l[0]* l[1]
            ans. append(temp)

        return ans
```
