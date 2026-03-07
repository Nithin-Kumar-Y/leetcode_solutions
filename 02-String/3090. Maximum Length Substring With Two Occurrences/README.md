## 3090. Maximum Length Substring With Two Occurrences


**Runtime- 18ms   Beats- 19.33%**


**Memory- 12.48MB  Beats- 56.30%**

---
## SOLUTION
```PYTHON

class Solution(object):

    def maximumLengthSubstring(self, s):

        """
        :type s: str
        :rtype: int
        """

        from collections import Counter

        maxi =0
        l = 0
        c = Counter()
        for r in range(len(s)):
            c[s[r]] += 1
            while c[s[r]]==3:
                c[s[l]]-=1
                if c[s[l]] ==0:
                    del c[s[l]]
                l+=1
            maxi = max(maxi, r-l+1)

        return maxi
```
