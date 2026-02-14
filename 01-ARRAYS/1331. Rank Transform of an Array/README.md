## 1331. Rank Transform of an Array

**RUNTIME  44MS  63.48%**

**SPACE  27.98MB  88.76%**

---
## SOLUTIONS
```PYTHON
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return []
        if len(arr)==1:
            return [1]
        setty = list(set(arr))
        setty.sort()
        dictty = {numb:rank for rank, numb in enumerate(setty, start = 1)}
        ans = []
        for i in arr:
            ans.append(dictty[i])
        return ans
```
