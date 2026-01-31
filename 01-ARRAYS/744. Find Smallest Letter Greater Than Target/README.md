## 744. Find Smallest Letter Greater Than Target

**Runtime-0ms 100%**

**Space-13.74mb- 37%**

---

## SOLUTION
```PYTHON
class Solution(object):

    def nextGreatestLetter(self, letters, target):
    
        """
        
        :type letters: List[str]
        
        :type target: str
        
        :rtype: str
        
        """
        
        for i in letters:
        
            if i > target:
            
                return i
                
        return letters[0]
```
