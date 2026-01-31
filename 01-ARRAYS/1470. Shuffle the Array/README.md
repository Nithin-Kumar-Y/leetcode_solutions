## 1470. Shuffle the Array

**runtime- 46ms Beats-15.17%**

**Memory- 12.69MB Beats-48.84%**

---

## SOLUTION

```PYTHON
class Solution(object):

    def shuffle(self, nums, n):
    
        ans = []
        
        for i in range(n):
        
            ans.append(nums[i])
            
            ans.append(nums[n+i])
            
        return ans
```
