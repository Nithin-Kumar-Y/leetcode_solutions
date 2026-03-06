## 3206. Alternating Groups I

**Runtime- 30ms   Beats- 83.47%**


**Memory- 12.33MB  Beats- 92.56%**

---
## SOLUTION
```PYTHON

class Solution(object):

    def numberOfAlternatingGroups(self, colors):

        """
        :type colors: List[int]
        :rtype: int
        """

        count = 0
        n = len(colors)
        for j in range(n):
            if (colors[(j+1)%n] == colors[(j-1)%n]) and (colors[(j+1) %n]!= colors[j]):
                count+=1

        return count
```
