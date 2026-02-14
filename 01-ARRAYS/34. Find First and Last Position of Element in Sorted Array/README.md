## 34. Find First and Last Position of Element in Sorted Array

**RUNTIME 2MS   18%**

**SPACE 13.9MB  13.9%**

---

## SOLUTIONS
```PYTHON
class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        l,r = -1, -1
        for i in range(len(nums)):
            if nums[i]== target:
                if l == -1:
                    l=i
                else:
                    r=i
            elif nums[i]>target:
                break
        if l != -1:
            if r == -1:
                return [l,l]
            else:
                return [l,r]
        else:
            return [-1,-1]
```
