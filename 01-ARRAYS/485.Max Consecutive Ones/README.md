## 485. Max Consecutive Ones

**Runtime -12ms  Beats-91.32%**

**Memory-13.64MB Beats-50.90%**

---
### SOLUTION
```PYTHON
class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
    
        """

        :type nums: List[int]

        :rtype: int

        """

        most, current = 0,0

        for i in nums:

            if i ==1:

                current+=1

                if current > most:

                    most = current

            else:

                current = 0

        return most
```        
