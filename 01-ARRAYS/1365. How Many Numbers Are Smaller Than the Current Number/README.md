## 1365. How Many Numbers Are Smaller Than the Current Number

**Runtime- 217ms**

**SPACE-12.4MB**

---

## SOLUTION

```PYTHON
class Solution(object):

    def smallerNumbersThanCurrent(self, nums):
    
        """
        
        :type nums: List[int]
        
        :rtype: List[int]
        
        """
        
        ans = [0]*len(nums)
        
        for i in range(len(nums)):
        
            for j in nums:
            
                if j<nums[i]:
                
                    ans[i]+=1
                    
        return ans
```
