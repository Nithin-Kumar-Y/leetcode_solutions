## 904. Fruit Into Baskets

**Runtime- 195ms  Beats- 92.57%**


**Memory= 17.09MB  Beats 74.84%**


---
## SOLUTIONS
```PYTHON

class Solution(object):

    def totalFruit(self, fruits):

        from collections import defaultdict

        c = defaultdict(int)
        best = 0
        l = 0
        n = len(fruits)
        for r in range(n):
            c[fruits[r]] +=1

            while len(c)>2:
                c[fruits[l]]-=1

                if c[fruits[l]]==0:
                    del c[fruits[l]]
                l+=1
            if best < r-l+1:
                best = r-l+1

        return best
```
