## 287. Find the Duplicate Number

**RUNTIME 78.72%**

**SPACE  27.28MB  13.27%**
---

## SOLUTIONS
```PYTHON

class Solution(object):

    def findDuplicate(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        total, summy = sum(nums), sum(set(nums))

        a,b = len(nums), len(set(nums))

        return (total-summy)/(a-b)
```
