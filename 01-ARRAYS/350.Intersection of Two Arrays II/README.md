## 350. Intersection of Two Arrays II

**Runtime- 23ms Beats-9.20%**

**Memory-12.64MB Beats30.95%**

---
### SOLUTION
```PYTHON
class Solution(object):

    def intersect(self, nums1, nums2):

        """

        :type nums1: List[int]

        :type nums2: List[int]

        :rtype: List[int]

        """

        if len(nums1)>len(nums2):

            reference = nums2

            runner = nums1

        else:

            reference = nums1

            runner = nums2

        ans = []

        for i in reference:

            if i in runner:

                runner.remove(i)

                ans.append(i)

        return ans
```

#### IDEAL SOLUTION:
```PYTHON
class Solution(object):

    def intersect(self, nums1, nums2):

        """

        :type nums1: List[int]

        :type nums2: List[int]

        :rtype: List[int]

        """

        dict1 = {}

        dict2={}

        for i in nums1:

            if i not in dict1:

                dict1[i] = 1

            else:

                dict1[i]+=1

        for i in nums2:

            if i not in dict2:

                dict2[i] = 1

            else:

                dict2[i]+=1

        sol = []

        for key,value in dict1.items():

            if key in dict2:

                val = min(value,dict2[key])

                sol.extend([key]*val)

        return sol
```
